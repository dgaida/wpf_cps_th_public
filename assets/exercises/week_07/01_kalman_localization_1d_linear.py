"""
1D Linear Kalman Filter for Target Localization
==============================================

This script implements a 1-dimensional linear Kalman Filter for target localization and state estimation
(position, velocity, and acceleration) from noisy sensor measurements.

Overview & Implementation:
--------------------------
The script simulates a target moving in one dimension according to continuous/discrete kinematic motion rules
and estimates its state vector $x_k$ over time using a Kalman Filter.

State Vector:
.. math::
    x_k = \\begin{bmatrix} p_k \\\\ v_k \\\\ a_k \\end{bmatrix} \\in \\mathbb{R}^3

where:
- $p_k$: Position at time step $k$
- $v_k$: Velocity at time step $k$
- $a_k$: Acceleration at time step $k$

Model Assumptions:
-------------------
1. Kinematic Motion Model (Constant Acceleration Model with Process Disturbance):
   The physical movement follows kinematic motion equations over sampling interval $\\Delta t$:
   .. math::
       p_k = p_{k-1} + v_{k-1} \\cdot \\Delta t + \\frac{1}{2} a_{k-1} \\cdot \\Delta t^2
   .. math::
       v_k = v_{k-1} + a_{k-1} \\cdot \\Delta t
   .. math::
       a_k = a_{k-1} + w_{a, k-1}

2. Linear State Dynamics:
   The discrete state transition equation is given by:
   .. math::
       x_k = A x_{k-1} + w_{k-1}

   where the state transition matrix $A \\in \\mathbb{R}^{3 \\times 3}$ is:
   .. math::
       A = \\begin{bmatrix}
       1 & \\Delta t & \\frac{1}{2}\\Delta t^2 \\\\
       0 & 1 & \\Delta t \\\\
       0 & 0 & 1
       \\end{bmatrix}

3. Linear Measurement Model:
   The measurement vector $y_k$ at time step $k$ depends on available sensor channels (`meas`):
   .. math::
       y_k = C x_k + v_k

   where $C$ is the measurement matrix mapping state variables to observations, e.g., for `meas = 'p_v_a'`:
   .. math::
       C = \\begin{bmatrix}
       1 & 0 & 0 \\\\
       0 & 1 & 0 \\\\
       0 & 0 & 1
       \\end{bmatrix}

4. Noise Statistics:
   - Process noise $w_k \\sim \\mathcal{N}(0, Q)$ is zero-mean Gaussian white noise with covariance matrix $Q$.
   - Measurement noise $v_k \\sim \\mathcal{N}(0, R)$ is zero-mean Gaussian white noise with covariance matrix $R$.
   - Process noise $w_k$ and measurement noise $v_k$ are assumed to be mutually uncorrelated.

Kalman Filter Equations:
-------------------------
1. Prediction (Time Update):
   .. math::
       \\hat{x}_k^- = A \\hat{x}_{k-1}^+
   .. math::
       P_k^- = A P_{k-1}^+ A^T + Q

2. Correction (Measurement Update):
   - Innovation / Measurement Residual:
     .. math::
         z_k = y_k - C \\hat{x}_k^-
   - Innovation Covariance:
     .. math::
         S_k = C P_k^- C^T + R
   - Kalman Gain:
     .. math::
         K_k = P_k^- C^T S_k^{-1}
   - Updated State Estimate (Posterior):
     .. math::
         \\hat{x}_k^+ = \\hat{x}_k^- + K_k z_k
   - Updated Estimate Covariance (Posterior):
     .. math::
         P_k^+ = (I - K_k C) P_k^-
"""

import math
from typing import Tuple, Union
import numpy as np
from numpy.random import randn
from numpy import dot
from scipy.linalg import inv

np.random.seed(42)


def select_y_R(
    x: float,
    vel: float,
    acc: float,
    sigma_x: float,
    sigma_yv: float,
    sigma_ya: float,
    meas: str
) -> Tuple[np.ndarray, np.ndarray]:
    """Creates and returns noisy measurement vector y and measurement noise covariance matrix R.

    Args:
        x (float): Current true position.
        vel (float): Current true velocity.
        acc (float): Current true acceleration.
        sigma_x (float): Standard deviation of position measurement noise.
        sigma_yv (float): Standard deviation of velocity measurement noise.
        sigma_ya (float): Standard deviation of acceleration measurement noise.
        meas (str): Selection string for measured quantities ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a').

    Returns:
        Tuple[np.ndarray, np.ndarray]:
            - y (np.ndarray): Measurement vector of shape (m, 1).
            - R (np.ndarray): Measurement noise covariance matrix of shape (m, m).

    Raises:
        ValueError: If `meas` is not an allowed measurement selection mode.
    """
    if meas == 'p_v':
        y = np.array([[x + randn() * sigma_x, vel + randn() * sigma_yv]]).T
        R = np.diag([sigma_x ** 2, sigma_yv ** 2])
    elif meas == 'p':
        y = np.array([[x + randn() * sigma_x]]).T
        R = np.diag([sigma_x ** 2])
    elif meas == 'a':
        y = np.array([[acc + randn() * sigma_ya]]).T
        R = np.diag([sigma_ya ** 2])
    elif meas == 'p_a':
        y = np.array([[x + randn() * sigma_x, acc + randn() * sigma_ya]]).T
        R = np.diag([sigma_x ** 2, sigma_ya ** 2])
    elif meas == 'v':
        y = np.array([[vel + randn() * sigma_yv]]).T
        R = np.diag([sigma_yv ** 2])
    elif meas == 'p_v_a':
        y = np.array([[x + randn() * sigma_x, vel + randn() * sigma_yv,
                       acc + randn() * sigma_ya]]).T
        R = np.diag([sigma_x ** 2, sigma_yv ** 2, sigma_ya ** 2])
    else:
        raise ValueError(f"Unknown measurement configuration: '{meas}'. Expected one of ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a').")

    return y, R


def select_C(meas: str) -> np.ndarray:
    """Creates and returns the measurement matrix C corresponding to the measurement configuration.

    Args:
        meas (str): Selection string for measured quantities ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a').

    Returns:
        np.ndarray: Measurement matrix C of shape (m, 3).

    Raises:
        ValueError: If `meas` is not an allowed measurement selection mode.
    """
    if meas == 'p_v':
        C = np.array([[1., 0., 0.],
                      [0., 1., 0.]])
    elif meas == 'p':
        C = np.array([[1., 0., 0.]])
    elif meas == 'a':
        C = np.array([[0., 0., 1.]])
    elif meas == 'p_a':
        C = np.array([[1., 0., 0.],
                      [0., 0., 1.]])
    elif meas == 'v':
        C = np.array([[0., 1., 0.]])
    elif meas == 'p_v_a':
        C = np.array([[1., 0., 0.],
                      [0., 1., 0.],
                      [0., 0., 1.]])
    else:
        raise ValueError(f"Unknown measurement configuration: '{meas}'. Expected one of ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a').")

    return C


def generate_acc(num_y: int) -> np.ndarray:
    """Generates a synthetic 1D acceleration profile over num_y time steps.

    Args:
        num_y (int): Number of time steps.

    Returns:
        np.ndarray: 1D array of acceleration values of length `num_y`.
    """
    acc = np.zeros((num_y, 1)).ravel()
    if num_y >= 5:
        acc[:5] = 0.5
    if num_y >= 20:
        acc[-20:-15] = -0.5
    if num_y >= 27:
        acc[25:27] = 0.25
    if num_y >= 67:
        acc[65:67] = -0.25

    return acc


def compute_y(
    sigma_yp: float,
    process_var: float,
    num_y: int = 1,
    dt: float = 1.0,
    meas: str = 'p'
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Simulates ground truth dynamics and produces noisy sensor measurements.

    Args:
        sigma_yp (float): Standard deviation of position measurement noise.
        process_var (float): Variance of process noise driving acceleration.
        num_y (int, optional): Number of simulation time steps. Defaults to 1.
        dt (float, optional): Sampling time interval $\\Delta t$. Defaults to 1.0.
        meas (str, optional): Selection string for measured variables ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a'). Defaults to 'p'.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]:
            - xs (np.ndarray): True positions over time, shape (num_y,).
            - ys (np.ndarray): Measurement vectors over time, shape (num_y, m, 1).
            - Rs (np.ndarray): Measurement noise covariance matrices over time, shape (num_y, m, m).
    """
    x, vel = 0.5, 0.0  # Initial ground truth position and velocity

    acc = generate_acc(num_y)
    sigma_yps = np.ones((num_y, 1)).ravel() * sigma_yp

    sigma_yv = 0.95  # Standard deviation for velocity measurement noise
    sigma_ya = 0.15  # Standard deviation for acceleration measurement noise

    p_std = math.sqrt(process_var)
    xs, ys, Rs = [], [], []

    for myacc, mysigma_y in zip(acc, sigma_yps):
        a = myacc + (randn() * p_std)
        x += vel * dt + a * 0.5 * dt**2
        vel += a * dt

        xs.append(x)

        y, R = select_y_R(x, vel, a, mysigma_y, sigma_yv, sigma_ya, meas)

        ys.append(y)
        Rs.append(R)

    return np.array(xs), np.array(ys), np.array(Rs)


def init_system(
    num_y: int = 50,
    meas: str = 'p'
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    """Initializes system matrices, initial state estimates, and covariance matrices for the Kalman filter.

    Args:
        num_y (int, optional): Number of time steps. Defaults to 50.
        meas (str, optional): Selection string for measured variables ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a'). Defaults to 'p'.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
            - b_true (np.ndarray): Ground truth position trajectory of shape (num_y,).
            - y (np.ndarray): Sensor measurements array of shape (num_y, m, 1).
            - u (np.ndarray): Control input vector array of shape (num_y,).
            - x (np.ndarray): Initial state vector estimate of shape (3, 1).
            - P (np.ndarray): Initial state error covariance matrix of shape (3, 3).
            - A (np.ndarray): State transition matrix of shape (3, 3).
            - C (np.ndarray): Output measurement matrix of shape (m, 3).
            - Rs (np.ndarray): Measurement noise covariance matrices array of shape (num_y, m, m).
            - Q (np.ndarray): Process noise covariance matrix of shape (3, 3).
            - dt (float): Sampling interval $\\Delta t$.
    """
    sigma_yp = 0.5        # Measurement standard deviation for position
    mu_b_post = 1.0       # Initial position estimate mean
    sigma_b_post = 2.0    # Initial position estimate standard deviation
    var_b_post = sigma_b_post ** 2  # Initial variance of position estimate
    var_a = 0.0001        # Process noise variance for acceleration
    dt = 0.2              # Sampling time interval Delta t

    b_true, y, Rs = compute_y(sigma_yp, var_a, num_y, dt, meas)

    u = np.zeros((num_y, 1)).ravel()

    # Initial state estimate [position, velocity, acceleration]^T
    x = np.array([[mu_b_post, 0.5, 0.3]]).T
    P = np.diag([var_b_post, 2.0, 1.0])

    # System transition matrix A
    A = np.array([[1.0, dt, 0.5 * dt**2],
                  [0.0, 1.0, dt],
                  [0.0, 0.0, 1.0]])

    # Measurement matrix C
    C = select_C(meas)

    # Process noise covariance matrix Q
    Q = np.diag([var_a * 0.5 * dt**2, var_a * dt, var_a])

    return b_true, y, u, x, P, A, C, Rs, Q, dt


def calc_estim_err(
    GT: np.ndarray,
    estim: np.ndarray,
    avg: bool = True
) -> Union[float, np.ndarray]:
    """Calculates estimation error between ground truth and estimated state values.

    Args:
        GT (np.ndarray): Ground truth values array.
        estim (np.ndarray): Estimated values array.
        avg (bool, optional): If True, calculates Root Mean Squared Error (RMSE).
                              If False, returns element-wise absolute differences. Defaults to True.

    Returns:
        Union[float, np.ndarray]:
            - Float RMSE scalar value if `avg` is True.
            - Array of elementwise errors if `avg` is False.
    """
    GT = GT.ravel()
    estim = estim.ravel()

    if avg:
        err = float(np.sqrt(np.mean((GT - estim)**2)))
    else:
        err = np.sqrt((GT - estim) ** 2)

    return err


def run_kalman(
    num_y: int = 30,
    meas: str = 'p_v'
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, int]:
    """Runs the 1D Kalman filter localization loop over specified number of steps.

    Args:
        num_y (int, optional): Number of estimation steps. Defaults to 30.
        meas (str, optional): Selection string for available measurements ('p', 'v', 'a', 'p_v', 'p_a', 'p_v_a'). Defaults to 'p_v'.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, int]:
            - xs (np.ndarray): Estimated state vector trajectory of shape (num_y, 3, 1).
            - b_true (np.ndarray): Ground truth position trajectory of shape (num_y,).
            - cov (np.ndarray): Estimated error covariance matrices of shape (num_y, 3, 3).
            - y (np.ndarray): Sensor measurement vector array of shape (num_y, m, 1).
            - Rs (np.ndarray): Measurement noise covariance matrices array of shape (num_y, m, m).
            - num_y (int): Total number of time steps simulated.
    """
    b_true, y, u, x, P, A, C, Rs, Q, dt = init_system(num_y=num_y, meas=meas)

    xs, cov = [], []
    for myy, R in zip(y, Rs):
        # 1. Prediction (Time Update)
        P = dot(A, P).dot(A.T) + Q
        x = dot(A, x)

        # 2. Correction (Measurement Update)
        S = dot(C, P).dot(C.T) + R
        K = dot(P, C.T).dot(inv(S))
        z = myy - dot(C, x)
        x += dot(K, z)
        P = P - dot(K, C).dot(P)

        xs.append(x)
        cov.append(P)

    xs_arr, cov_arr = np.array(xs), np.array(cov)

    print('estimation error:', calc_estim_err(b_true, xs_arr[:, 0]))

    # print('b_estim:', xs_arr[:, 0])
    # print('v_estim:', xs_arr[:, 1])
    # print('a_estim:', xs_arr[:, 2])
    # print('var_b:', cov_arr[:, 0, 0])
    # print('var_v:', cov_arr[:, 1, 1])
    # print('var_a:', cov_arr[:, 2, 2])

    return xs_arr, b_true, cov_arr, y, Rs, num_y


if __name__ == '__main__':
    run_kalman(num_y=80, meas='p_a')
