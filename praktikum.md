---
layout: page
title: Praktikum
description: Informationen, Übersicht und Materialien zu den Praktikumsaufgaben im Modul Cyber-Physische Systeme (CPS).
nav_order: 4
---

# Praktikum

Auf dieser Seite finden Sie die Übersicht und Materialien zu allen Praktikumsaufgaben des Moduls **Cyber-Physische Systeme (CPS)**.

## 👥 Organisation & Durchführung

Die Praktika werden in **3er-Teams** durchgeführt. Jedes Team absolviert im Laufe des Semesters insgesamt **vier Praktikumsaufgaben**:  
- **Drei einführende Praktika** (*Einführung*)  
- **Ein fortgeschrittenes Praktikum** (*Fortgeschritten*)  

---

## 🟢 Einführende Praktika (Einführung)

### Deep Robotics Lite3 LiDAR (Inbetriebnahme, Fernsteuerung & ROS Integration)

In diesem einführenden Praktikum lernen die Studierenden die Grundlagen des vierbeinigen Laufroboters (Quadruped) Deep Robotics Lite3 LiDAR kennen. Sie führen die sichere Inbetriebnahme durch, steuern den Roboter mit dem Handheld, verbinden sich über das Roboter-WLAN per SSH und NoMachine mit dem Perception Host und starten dort die Treiber von LiDAR und Tiefenkamera, um ROS 2-Topics (wie `/rslidar_points`, `/imu/data` und das Tiefenbild) über CLI-Tools und ein eigenes Python-Skript auszulesen.

**Genutzte Hardware:**
Deep Robotics Lite3 LiDAR (Vierbeiniger Laufroboter / Quadruped)
[![Deep Robotics Lite3](https://www.deeprobotics.us/wp-content/uploads/2025/07/deep-robotics-lite3-quadruped-robot.png)](https://www.deeprobotics.us/products/lite-3/)
*Quelle / Bildnachweis:* [Deep Robotics Lite3 Produktseite](https://www.deeprobotics.us/products/lite-3/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 deeprobotics_lite3.zip]({{ '/assets/praktikum/deeprobotics_lite3.zip' | relative_url }})  

---

### Kalman-Filter 2D Lokalisierung

Im Rahmen dieses Praktikums wird ein 2D-Kalman-Filter zur präzisen Lokalisierung eines autonom fahrenden Fahrzeugs in der fotorealistischen Simulationsumgebung AirSim (Neighborhood) entwickelt. Die Studierenden verarbeiten verrauschte GPS-, IMU- und Odometriedaten, um den Systemzustand fortlaufend zu schätzen und im Echtzeit-Plot zu evaluieren.

**Genutzte Hardware / Simulation:**
AirSim 2D Simulation (Simuliertes Fahrzeug)
![AirSim Simulation]({{ '/assets/praktikum/airsimcarsim.png' | relative_url }})

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 kalman_localization_2d.zip]({{ '/assets/praktikum/kalman_localization_2d.zip' | relative_url }})  

---

### LIMO Cobot Einführung (Inbetriebnahme, Tastatursteuerung & Demos)

In diesem einführenden Praktikum lernen die Studierenden die Grundlagen des mobilen Robotersystems AgileX LIMO Cobot kennen. Sie stellen eine Remote-Desktop-Verbindung via NoMachine her, steuern den Roboter per Tastatur über ROS und führen unter ROS 1 und ROS 2 praktische Demos zur 2D-Kartierung (SLAM), zur Farb- und Texterkennung mit der RGB-D-Kamera und zur Steuerung des Roboterarms myCobot 280 durch.

**Genutzte Hardware:**
AgileX LIMO Cobot (Mobiles Robotiksystem)
[![AgileX LIMO Cobot](https://static.elephantrobotics.com/wp-content/uploads/2024/01/LIMO-Cobot%E4%B8%BB%E5%9B%BE20240118-800x450.png)](https://www.elephantrobotics.com/en/limo-cobot-en/)
*Quelle / Bildnachweis:* [Elephant Robotics LIMO Cobot](https://www.elephantrobotics.com/en/limo-cobot-en/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 limo_cobot_intro.zip]({{ '/assets/praktikum/limo_cobot_intro.zip' | relative_url }})  

---

### Niryo NED2 Fertigungsprozess

In diesem Praktikum erstellen die Studierenden einen automatisierten Industrie-Fertigungsprozess mit dem kollaborativen 6-Achs-Roboterarm Niryo NED2. Unter Verwendung der Python-API (`pyniryo`) wird eine Werkstück-Aussortierung mit dem Niryo Vision-Set (Farberkennung) und einem Infrarot-Sensor-gesteuerten Förderband umgesetzt.

**Genutzte Hardware:**
Niryo NED2 (Kollaborativer 6-Achs-Roboterarm)
[![Niryo NED2](https://docs.niryo.com/robots/ned2/source/_static/img/ned2.png)](https://docs.niryo.com/robots/ned2/)
*Quelle / Bildnachweis:* [Niryo NED2 Offizielle Dokumentation](https://docs.niryo.com/robots/ned2/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 niryo_ned2.zip]({{ '/assets/praktikum/niryo_ned2.zip' | relative_url }})  

---

### Raspberry Pi 5 & AI HAT+ 2 (Edge-AI & LLMs)

In diesem Praktikum evaluieren die Studierenden moderne Edge-AI-Hardwarebeschleunigung auf dem Raspberry Pi 5 in Kombination mit dem Raspberry Pi AI HAT+ 2 (26 TOPS Hailo-8 NPU). Das Praktikum umfasst zwei zentrale Kernaufgaben: (1) Echtzeit-Objektdetektion im Kamerastream (Intel RealSense D415) mittels Ultralytics YOLO (YOLOv8 / YOLOE / YOLO26) und (2) die lokale Ausführung generativer Sprachmodelle (LLMs wie Llama-3.2-1B oder Qwen2.5-1.5B) via Hailo GenAI, inkl. Messung der Inferenzrate (FPS bzw. Tokens/s) und Systemauslastung.

**Genutzte Hardware:**
Raspberry Pi 5, Raspberry Pi AI HAT+ 2 (Hailo-8 NPU) & Intel RealSense D415

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 rpi_ai_hat.zip]({{ '/assets/praktikum/rpi_ai_hat.zip' | relative_url }})  

---

### TurtleBot 4 & ROS 2

Dieses Praktikum vermittelt die Grundlagen verteilter Robotiksysteme in Robot Operating System 2 (ROS 2 Humble) auf dem TurtleBot 4. Die Studierenden entwickeln eigene Python-Nodes (`rclpy`), arbeiten mit Publish-Subscribe-Topics sowie Services und steuern Roboter kinematic-basiert in der Simulation und auf realer Hardware.

**Genutzte Hardware:**
TurtleBot 4 (Mobiles Robotiksystem)
[![TurtleBot 4](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)](https://turtlebot.github.io/turtlebot4-user-manual/)
*Quelle / Bildnachweis:* [TurtleBot 4 User Manual (Clearpath Robotics / Open Robotics)](https://turtlebot.github.io/turtlebot4-user-manual/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 turtlebot.zip]({{ '/assets/praktikum/turtlebot.zip' | relative_url }})  

---

### Turtle Train (Multi-Roboter Formationsfahrt mit TF2)

In diesem Praktikum setzen die Studierenden das ROS 2 TF2 Transformations-Framework zur Realisierung einer Mehrroboter-Formationsfahrt (**Turtle Train**) ein. Auf Basis der beliebten ROS-Videoreihe von Shawn Hymel (DigiKey) entwickeln die Studierenden TF2 Broadcaster und Listener zur dynamischen Abstandskontrolle in der Turtlesim-Simulation sowie auf realen mobilen Robotern (TurtleBot 4 und LIMO Cobot).

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 turtle_train.zip]({{ '/assets/praktikum/turtle_train.zip' | relative_url }})  

---

### WidowX-250s Roboterarm

Dieses Praktikum behandelt die kinematiche Modellierung und Steuerung des hochpräzisen 6DOF-Roboterarms WidowX-250s von Interbotix. Mittels Interbotix Python SDK berechnen die Studierenden Vorwärts- und Inverse Kinematik, planen dreidimensionale Trajektorien und setzen Pick-and-Place-Manöver um.

**Genutzte Hardware:**
WidowX-250s (6DOF Roboterarm)
[![WidowX-250s Robot Arm](https://docs.trossenrobotics.com/interbotix_xsarms_docs/_images/xsarm_family.png)](https://docs.trossenrobotics.com/interbotix_xsarms_docs/)
*Quelle / Bildnachweis:* [Interbotix X-Series Manipulators Documentation (Trossen Robotics)](https://docs.trossenrobotics.com/interbotix_xsarms_docs/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 widowx250s.zip]({{ '/assets/praktikum/widowx250s.zip' | relative_url }})  

---

## 🚀 Fortgeschrittene Praktika (Fortgeschritten)

### Leader-Follower-Synchronisation (WidowX-250s & Niryo NED2)

In diesem Praktikum setzen die Studierenden eine Echtzeit-Leader-Follower-Synchronisation zwischen zwei Roboterarmen um: Der WidowX-250s wird manuell geführt (Leader), während der Niryo NED2 (Follower) dessen Bewegungen, Greiferorientierung und Greiferzustand in Echtzeit nachvollzieht. Die Aufgabenstellung umfasst die kinematische Modellierung (Product of Exponentials), numerische inverse Kinematik, Arbeitsraumbegrenzung sowie die Ansteuerung über ROS 2, rosbridge oder pyniryo.

**Genutzte Hardware:**
WidowX-250s & Niryo NED2
[![WidowX-250s Robot Arm](https://docs.trossenrobotics.com/interbotix_xsarms_docs/_images/xsarm_family.png)](https://docs.trossenrobotics.com/interbotix_xsarms_docs/)
*Quelle / Bildnachweis:* [Interbotix X-Series Manipulators Documentation (Trossen Robotics)](https://docs.trossenrobotics.com/interbotix_xsarms_docs/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 niryo_ned2_wx250s.zip]({{ '/assets/praktikum/niryo_ned2_wx250s.zip' | relative_url }})  

---

### LIMO Cobot (Autonomes Greifen & Navigation)

Dieses Praktikum kombiniert mobile Autonomie und Manipulation auf der AgileX LIMO Cobot Plattform. Die Studierenden nutzen 2D-LiDAR zur Raumkartierung (SLAM) und Navigation sowie eine RGB-D-Tiefenkamera zur 3D-Objekterkennung, um Zielobjekte autonom anzufahren und mit dem integrierten Roboterarm zu greifen.

**Genutzte Hardware:**
AgileX LIMO Cobot (Mobile Manipulationsplattform)
[![AgileX LIMO Cobot](https://static.elephantrobotics.com/wp-content/uploads/2024/01/LIMO-Cobot%E4%B8%BB%E5%9B%BE20240118-800x450.png)](https://www.elephantrobotics.com/en/limo-cobot-en/)
*Quelle / Bildnachweis:* [Elephant Robotics LIMO Cobot](https://www.elephantrobotics.com/en/limo-cobot-en/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 limo_cobot.zip]({{ '/assets/praktikum/limo_cobot.zip' | relative_url }})  

---

### LIMO Überholt TurtleBot

In dieser Praktikumsaufgabe wird ein dynamisches Roboter-Interaktionsszenario zwischen dem LIMO Cobot und dem vorausfahrenden TurtleBot 4 umgesetzt. Der LIMO Cobot schätzt mittels Sensorik kontinuierlich die Geschwindigkeit des TurtleBots, berechnet eine Trajektorienprognose und führt bei gewähltem Abstand ein synchronisiertes Überholmanöver mit Wende- und Einscherphase durch.

**Genutzte Hardware:**
AgileX LIMO Cobot & TurtleBot 4
[![TurtleBot 4](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)](https://turtlebot.github.io/turtlebot4-user-manual/)
*Quelle / Bildnachweis:* [TurtleBot 4 User Manual (Clearpath Robotics / Open Robotics)](https://turtlebot.github.io/turtlebot4-user-manual/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 limo_overtaking_turtlebot.zip]({{ '/assets/praktikum/limo_overtaking_turtlebot.zip' | relative_url }})  

---

### Niryo Objektdetektion & Turmbau

Dieses Praktikum vereint Computer Vision, Deep Learning und kollaborative Robotik für eine Sortier- und Stapelaufgabe. Die Studierenden trainieren ein Convolutional Neural Network (CNN / Transfer Learning) zur Erkennung verschiedener Objektklassen mit dem Niryo Vision-Set, ermitteln Objekthöhen über eine Overhead RealSense D435 Tiefenbildkamera und bauen mit dem Niryo NED2 gestapelte Türme auf.

**Genutzte Hardware:**
Niryo NED2 & Intel RealSense D435
[![Niryo NED2](https://docs.niryo.com/robots/ned2/source/_static/img/ned2.png)](https://docs.niryo.com/robots/ned2/)
*Quelle / Bildnachweis:* [Niryo NED2 Offizielle Dokumentation](https://docs.niryo.com/robots/ned2/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 niryo_object_detection.zip]({{ '/assets/praktikum/niryo_object_detection.zip' | relative_url }})  

---

### TurtleBot Orientierungsschätzung (Kalman)

In dieser Aufgabe wird der TurtleBot 4 um einen externen Sensorknoten (Arduino Nicla Sense ME) mit 6-Achs-IMU und Magnetometer erweitert. Die Studierenden implementieren ein Kalman-Filter zur Echtzeit-Orientierungsschätzung (Gierwinkel / Quaternion) und vergleichen die Schätzergebnisse grafisch mit der internen TurtleBot-Odometrierelation.

**Genutzte Hardware:**
TurtleBot 4 & Arduino Nicla Sense ME
[![Arduino Nicla Sense ME](https://store.arduino.cc/cdn/shop/files/ABX00050_03.front_1200x900.jpg)](https://docs.arduino.cc/hardware/nicla-sense-me/)
*Quelle / Bildnachweis:* [Arduino Docs (Arduino S.r.l.)](https://docs.arduino.cc/hardware/nicla-sense-me/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 turtlebot_orientation_kalman.zip]({{ '/assets/praktikum/turtlebot_orientation_kalman.zip' | relative_url }})  

---

### TurtleBot Pfadplanung & SLAM

Dieses Praktikum beinhaltet die vollständige Navigationspipeline autonomer mobiler Roboter von der Kartierung bis zur Bewegungsplanung. Nach der Erstellung eines Occupancy Grids mit `slam_toolbox` diskretisieren die Studierenden den Raum als Suchgraph und implementieren sowie visualisieren Suchalgorithmen (Dijkstra und A*) im Vergleich zu ROS 2 Nav2.

**Genutzte Hardware:**
TurtleBot 4 (Mobiles Robotiksystem)
[![TurtleBot 4](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)](https://turtlebot.github.io/turtlebot4-user-manual/)
*Quelle / Bildnachweis:* [TurtleBot 4 User Manual (Clearpath Robotics / Open Robotics)](https://turtlebot.github.io/turtlebot4-user-manual/)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 turtlebot_path_planning.zip]({{ '/assets/praktikum/turtlebot_path_planning.zip' | relative_url }})  
