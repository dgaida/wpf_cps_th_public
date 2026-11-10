"""Helper functions for 1D linear kinematic system simulation, plotting, and animation."""

from typing import Tuple
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def plot_simulation_results(
    times: np.ndarray,
    p_k: np.ndarray,
    v_k: np.ndarray,
    a_k_profile: np.ndarray,
    figsize: Tuple[int, int] = (11, 8),
) -> Tuple[plt.Figure, np.ndarray]:
    """Plots simulated position, velocity, and acceleration over time.

    Args:
        times: 1D array of time stamps in seconds.
        p_k: 1D array of positions in meters.
        v_k: 1D array of velocities in m/s.
        a_k_profile: 1D array of accelerations per discrete time step in m/s^2.
        figsize: Figure dimensions (width, height) in inches.

    Returns:
        A tuple containing the Matplotlib Figure and array of Axes objects.
    """
    fig, axs = plt.subplots(3, 1, figsize=figsize, sharex=True)

    # 1. Plot: Position
    axs[0].plot(times, p_k, "b-o", markersize=5, linewidth=2, label=r"Position $p_k$ [m]")
    axs[0].set_ylabel("Position $p_k$ [m]", fontsize=12)
    axs[0].set_title(
        r"1D Lineares System: Zustandsverläufe über der Zeit",
        fontsize=14,
        fontweight="bold",
    )
    axs[0].grid(True, linestyle="--", alpha=0.7)
    axs[0].legend(loc="upper left")

    # 2. Plot: Geschwindigkeit
    axs[1].plot(times, v_k, "g-s", markersize=5, linewidth=2, label=r"Geschwindigkeit $v_k$ [m/s]")
    axs[1].set_ylabel("Geschwindigkeit $v_k$ [m/s]", fontsize=12)
    axs[1].grid(True, linestyle="--", alpha=0.7)
    axs[1].legend(loc="upper left")

    # 3. Plot: Beschleunigung (stufenförmig)
    axs[2].step(
        times[:-1],
        a_k_profile,
        where="post",
        color="crimson",
        linewidth=2,
        label=r"Vorgegebene Beschleunigung $a_k$ [m/s²]",
    )
    axs[2].scatter(times[:-1], a_k_profile, color="crimson", s=35, zorder=3)
    axs[2].set_ylabel("Beschleunigung $a_k$ [m/s²]", fontsize=12)
    axs[2].set_xlabel("Zeit $t$ [s]", fontsize=12)
    axs[2].grid(True, linestyle="--", alpha=0.7)
    axs[2].legend(loc="upper left")

    plt.tight_layout()
    return fig, axs


def create_bicycle_animation(
    times: np.ndarray,
    p_k: np.ndarray,
    v_k: np.ndarray,
    fps: int = 15,
) -> animation.FuncAnimation:
    """Creates a 2D bicycle animation moving along a 1D track based on simulated kinematics.

    Args:
        times: 1D array of simulation time points.
        p_k: 1D array of positions in meters.
        v_k: 1D array of velocities in m/s.
        fps: Frames per second for smooth rendering.

    Returns:
        A matplotlib FuncAnimation object representing the animated bicycle.
    """
    fig_anim, ax_anim = plt.subplots(figsize=(12, 3.8))

    p_min = min(float(np.min(p_k)), 0.0) - 2.0
    p_max = max(float(np.max(p_k)), 10.0) + 5.0

    ax_anim.set_xlim(p_min, p_max)
    ax_anim.set_ylim(-0.3, 3.8)
    ax_anim.set_aspect("equal")
    ax_anim.set_xlabel("1D Position $p$ [m]", fontsize=12)
    ax_anim.set_title("Fahrrad-Fahrt entlang der 1D-Umgebung", fontsize=13, fontweight="bold")
    ax_anim.grid(True, linestyle=":", alpha=0.6)

    # Fahrbahn und Markierungen
    ax_anim.axhline(0.0, color="dimgray", linewidth=3.5, label="Fahrbahn")
    ticks_x = np.arange(int(np.floor(p_min)), int(np.ceil(p_max)) + 1, 5)
    for tx in ticks_x:
        if p_min <= tx <= p_max:
            ax_anim.plot([tx, tx], [0.0, -0.2], color="dimgray", linewidth=1.5)
            ax_anim.text(tx, -0.3, f"{tx}m", ha="center", va="top", fontsize=9, color="dimgray")

    # Fahrrad-Geometrie
    r_wheel = 0.6  # Laufrad-Radius [m]
    wheelbase_half = 1.0  # Halber Radstand [m]

    # Patches für Laufräder
    rear_wheel = Circle((0, r_wheel), r_wheel, color="#222222", fill=False, lw=3)
    front_wheel = Circle((0, r_wheel), r_wheel, color="#222222", fill=False, lw=3)
    rear_hub = Circle((0, r_wheel), 0.08, color="black", fill=True)
    front_hub = Circle((0, r_wheel), 0.08, color="black", fill=True)

    # Speichen (rotieren mit Drehwinkel)
    (rear_spokes,) = ax_anim.plot([], [], color="gray", lw=1.2)
    (front_spokes,) = ax_anim.plot([], [], color="gray", lw=1.2)

    # Fahrradrahmen, Gabel, Sattel und Lenker
    (frame_line,) = ax_anim.plot([], [], color="#0055bb", lw=3.5, solid_capstyle="round")
    (fork_line,) = ax_anim.plot([], [], color="#003388", lw=3.0, solid_capstyle="round")
    (saddle_line,) = ax_anim.plot([], [], color="black", lw=4.5, solid_capstyle="round")
    (handlebar_line,) = ax_anim.plot([], [], color="black", lw=3.5, solid_capstyle="round")

    # Status-Text für Zeit, Position und Geschwindigkeit
    status_text = ax_anim.text(
        0.02,
        0.88,
        "",
        transform=ax_anim.transAxes,
        fontsize=11,
        fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="navy", alpha=0.9),
    )

    ax_anim.add_patch(rear_wheel)
    ax_anim.add_patch(front_wheel)
    ax_anim.add_patch(rear_hub)
    ax_anim.add_patch(front_hub)

    # Interpolation für flüssige Animation
    total_duration = max(float(times[-1] - times[0]), 0.1)
    t_fine = np.linspace(times[0], times[-1], int(total_duration * fps) + 1)
    p_fine = np.interp(t_fine, times, p_k)
    v_fine = np.interp(t_fine, times, v_k)

    def init_anim():
        frame_line.set_data([], [])
        fork_line.set_data([], [])
        saddle_line.set_data([], [])
        handlebar_line.set_data([], [])
        rear_spokes.set_data([], [])
        front_spokes.set_data([], [])
        status_text.set_text("")
        return (
            rear_wheel,
            front_wheel,
            rear_hub,
            front_hub,
            frame_line,
            fork_line,
            saddle_line,
            handlebar_line,
            rear_spokes,
            front_spokes,
            status_text,
        )

    def update_anim(frame_idx):
        xc = p_fine[frame_idx]
        current_t = t_fine[frame_idx]
        current_v = v_fine[frame_idx]

        yw = r_wheel
        xr = xc - wheelbase_half
        xf = xc + wheelbase_half

        # Positionierung der Räder
        rear_wheel.center = (xr, yw)
        front_wheel.center = (xf, yw)
        rear_hub.center = (xr, yw)
        front_hub.center = (xf, yw)

        # Speichenrotation basierend auf zurückgelegter Distanz
        theta = -xc / r_wheel
        angles = np.array([theta, theta + np.pi / 2, theta + np.pi / 4, theta + 3 * np.pi / 4])

        spokes_r_x = []
        spokes_r_y = []
        spokes_f_x = []
        spokes_f_y = []
        for ang in angles:
            spokes_r_x.extend([xr - r_wheel * np.cos(ang), xr + r_wheel * np.cos(ang), np.nan])
            spokes_r_y.extend([yw - r_wheel * np.sin(ang), yw + r_wheel * np.sin(ang), np.nan])
            spokes_f_x.extend([xf - r_wheel * np.cos(ang), xf + r_wheel * np.cos(ang), np.nan])
            spokes_f_y.extend([yw - r_wheel * np.sin(ang), yw + r_wheel * np.sin(ang), np.nan])

        rear_spokes.set_data(spokes_r_x, spokes_r_y)
        front_spokes.set_data(spokes_f_x, spokes_f_y)

        # Rahmenpunkte
        xb = xc - 0.2  # Tretlager
        yb = yw
        xs = xc - 0.5  # Sattelrohr
        ys = yw + 1.05
        xh = xc + 0.65  # Steuerrohr
        yh = yw + 1.15

        # Diamantrahmen
        frame_x = [xr, xb, xs, xr, xb, xh, xs]
        frame_y = [yw, yb, ys, yw, yb, yh, ys]
        frame_line.set_data(frame_x, frame_y)

        # Gabel und Lenker
        fork_x = [xf, xh, xh - 0.08, xh + 0.15]
        fork_y = [yw, yh, yh + 0.22, yh + 0.22]
        fork_line.set_data(fork_x, fork_y)

        # Lenkergriff
        handlebar_line.set_data([xh + 0.05, xh + 0.2], [yh + 0.22, yh + 0.20])

        # Sattel
        saddle_line.set_data([xs - 0.22, xs + 0.18], [ys + 0.12, ys + 0.12])

        # Status-Anzeige
        status_text.set_text(
            f"Zeit t: {current_t:4.1f} s | Position p: {xc:5.2f} m | "
            f"Geschw. v: {current_v:4.2f} m/s ({current_v*3.6:4.1f} km/h)"
        )

        return (
            rear_wheel,
            front_wheel,
            rear_hub,
            front_hub,
            frame_line,
            fork_line,
            saddle_line,
            handlebar_line,
            rear_spokes,
            front_spokes,
            status_text,
        )

    anim = animation.FuncAnimation(
        fig_anim,
        update_anim,
        frames=len(t_fine),
        init_func=init_anim,
        interval=1000 / fps,
        blit=True,
    )

    plt.close(fig_anim)
    return anim


def plot_comparison_with_measurements(
    times: np.ndarray,
    p_true: np.ndarray,
    v_true: np.ndarray,
    a_true: np.ndarray,
    p_calc: np.ndarray,
    v_calc: np.ndarray,
    a_meas: np.ndarray,
    p_meas: np.ndarray,
    figsize: Tuple[int, int] = (12, 10),
) -> Tuple[plt.Figure, np.ndarray]:
    """Plots comparison between ground truth, calculated states from measured acceleration, and sensor measurements.

    Args:
        times: 1D array of time steps in seconds.
        p_true: 1D array of ground truth positions in meters.
        v_true: 1D array of ground truth velocities in m/s.
        a_true: 1D array of ground truth accelerations in m/s^2.
        p_calc: 1D array of positions calculated from measured acceleration in meters.
        v_calc: 1D array of velocities calculated from measured acceleration in m/s.
        a_meas: 1D array of noisy measured accelerations in m/s^2.
        p_meas: 1D array of noisy measured positions in meters.
        figsize: Figure size tuple (width, height) in inches.

    Returns:
        A tuple containing the Matplotlib Figure and array of Axes objects.
    """
    fig, axs = plt.subplots(3, 1, figsize=figsize, sharex=True)

    # 1. Plot: Position
    axs[0].plot(times, p_true, "g-", linewidth=2.5, label="Tatsächliche Position (Ground Truth)")
    axs[0].plot(
        times,
        p_calc,
        "b--",
        linewidth=2,
        label=r"Berechnete Position (aus $a_{\mathrm{meas}}$)",
    )
    axs[0].scatter(
        times,
        p_meas,
        color="crimson",
        s=25,
        alpha=0.7,
        zorder=3,
        label=r"Gemessene Position $p_{\mathrm{meas}}$ (Sensor)",
    )
    axs[0].set_ylabel("Position [m]", fontsize=12)
    axs[0].set_title(
        "Vergleich: Ground Truth vs. berechnete Zustände aus Beschleunigungsmessung vs. Positionsmessung",
        fontsize=13,
        fontweight="bold",
    )
    axs[0].grid(True, linestyle="--", alpha=0.7)
    axs[0].legend(loc="upper left")

    # 2. Plot: Geschwindigkeit
    axs[1].plot(
        times, v_true, "g-", linewidth=2.5, label="Tatsächliche Geschwindigkeit (Ground Truth)"
    )
    axs[1].plot(
        times,
        v_calc,
        "b--",
        linewidth=2,
        label=r"Berechnete Geschwindigkeit (aus $a_{\mathrm{meas}}$)",
    )
    axs[1].set_ylabel("Geschwindigkeit [m/s]", fontsize=12)
    axs[1].grid(True, linestyle="--", alpha=0.7)
    axs[1].legend(loc="upper left")

    # 3. Plot: Beschleunigung
    num_a_steps = len(times) - 1
    # Beschleunigungsgraph: Ground Truth stufenförmig
    axs[2].step(
        times[:-1],
        a_true[:num_a_steps],
        where="post",
        color="green",
        linewidth=2.5,
        label="Tatsächliche Beschleunigung (Ground Truth)",
    )
    axs[2].step(
        times[:-1],
        a_meas[:num_a_steps],
        where="post",
        color="royalblue",
        linestyle="--",
        linewidth=1.8,
        label=r"Gemessene Beschleunigung $a_{\mathrm{meas}}$ (verrauscht)",
    )
    axs[2].scatter(
        times[:-1],
        a_meas[:num_a_steps],
        color="royalblue",
        s=25,
        alpha=0.8,
        zorder=3,
    )
    axs[2].set_ylabel("Beschleunigung [m/s²]", fontsize=12)
    axs[2].set_xlabel("Zeit $t$ [s]", fontsize=12)
    axs[2].grid(True, linestyle="--", alpha=0.7)
    axs[2].legend(loc="upper left")

    plt.tight_layout()
    return fig, axs
