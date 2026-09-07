---
layout: page
title: Praktikum
description: Informationen, Übersicht und Materialien zu den Praktikumsaufgaben im Modul Cyber-Physische Systeme (CPS).
nav_order: 4
---

# Praktikum

Auf dieser Seite finden Sie die Übersicht und Materialien zu allen Praktikumsaufgaben des Moduls **Cyber-Physische Systeme (CPS)**.

## 👥 Organisation & Durchführung

Die Praktika werden in **3er-Teams** durchgeführt. Jedes Team absolviert im Laufe des Semesters insgesamt **drei Praktikumsaufgaben**:  
- **Zwei einführende Praktika** (*Einführung*)  
- **Ein fortgeschrittenes Praktikum** (*Fortgeschritten*)  

---

## 🟢 Einführende Praktika (Einführung)

### Kalman-Filter 2D Lokalisierung

Im Rahmen dieses Praktikums wird ein 2D-Kalman-Filter zur präzisen Lokalisierung eines autonom fahrenden Fahrzeugs in der fotorealistischen Simulationsumgebung AirSim (Neighborhood) entwickelt. Die Studierenden verarbeiten verrauschte GPS-, IMU- und Odometriedaten, um den Systemzustand fortlaufend zu schätzen und im Echtzeit-Plot zu evaluieren.

**Genutzte Hardware / Simulation:**
AirSim 2D Simulation (Simuliertes Fahrzeug)
[![AirSim Logo](https://raw.githubusercontent.com/microsoft/AirSim/main/docs/images/airsim_logo.png)](https://github.com/microsoft/AirSim)
*Quelle / Bildnachweis:* [Microsoft AirSim GitHub Repository](https://github.com/microsoft/AirSim)

#### Download

Laden Sie das Quellcode-Paket für das Praktikum herunter:

- [📄 kalman_localization_2d.zip]({{ '/assets/praktikum/kalman_localization_2d.zip' | relative_url }})  

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

### TurtleBot 4 & ROS 2

Dieses Praktikum vermittelt die Grundlagen verteilter Robotiksysteme in Robot Operating System 2 (ROS 2 Humble) auf dem TurtleBot 4. Die Studierenden entwickeln eigene Python-Nodes (`rclpy`), arbeiten mit Publish-Subscribe-Topics sowie Services und steuern Roboter kinematic-basiert in der Simulation und auf realer Hardware.

**Genutzte Hardware:**
TurtleBot 4 (Mobiles Robotiksystem)
[![TurtleBot 4](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)](https://turtlebot.github.io/turtlebot4-user-manual/)
*Quelle / Bildnachweis:* [TurtleBot 4 User Manual (Clearpath Robotics / Open Robotics)](https://turtlebot.github.io/turtlebot4-user-manual/)

---

### WidowX-250s Roboterarm

Dieses Praktikum behandelt die kinematiche Modellierung und Steuerung des hochpräzisen 6DOF-Roboterarms WidowX-250s von Interbotix. Mittels Interbotix Python SDK berechnen die Studierenden Vorwärts- und Inverse Kinematik, planen dreidimensionale Trajektorien und setzen Pick-and-Place-Manöver um.

**Genutzte Hardware:**
WidowX-250s (6DOF Roboterarm)
[![WidowX-250s Robot Arm](https://docs.trossenrobotics.com/interbotix_xsarms_docs/_images/xsarm_family.png)](https://docs.trossenrobotics.com/interbotix_xsarms_docs/)
*Quelle / Bildnachweis:* [Interbotix X-Series Manipulators Documentation (Trossen Robotics)](https://docs.trossenrobotics.com/interbotix_xsarms_docs/)

---

## 🚀 Fortgeschrittene Praktika (Fortgeschritten)

### Embedded AI & Robotik mit Arduino

In diesem Praktikum entwickeln die Studierenden eine verteilte, intelligente Roboterzelle zur automatisierten Bearbeitung. Ein Arduino Nicla Sense ME erfasst Lagedaten am Greifer des WidowX-250 via TinyML (Edge Impulse), während ein Arduino Portenta H7 mit Vision Shield Werkstücke erkennt und den Niryo NED2 über digitale Signale koordiniert.

**Genutzte Hardware:**
Arduino Portenta H7, Portenta Vision Shield & Arduino Nicla Sense ME
[![Arduino Portenta H7](https://docs.arduino.cc/static/235f3dfd9f9661bd687258bf7a1cd1f5/39564/portenta-h7.jpg)](https://docs.arduino.cc/hardware/portenta-h7/)
*Quelle / Bildnachweis:* [Arduino Docs (Arduino S.r.l.)](https://docs.arduino.cc/hardware/portenta-h7/)

---

### LIMO Cobot (Autonomes Greifen & Navigation)

Dieses Praktikum kombiniert mobile Autonomie und Manipulation auf der AgileX LIMO Cobot Plattform. Die Studierenden nutzen 2D-LiDAR zur Raumkartierung (SLAM) und Navigation sowie eine RGB-D-Tiefenkamera zur 3D-Objekterkennung, um Zielobjekte autonom anzufahren und mit dem integrierten Roboterarm zu greifen.

**Genutzte Hardware:**
AgileX LIMO Cobot (Mobile Manipulationsplattform)
[![AgileX LIMO Cobot](https://global.agilex.ai/assets/limo_cobot.jpg)](https://global.agilex.ai/products/limo-cobot)
*Quelle / Bildnachweis:* [AgileX Robotics LIMO Cobot](https://global.agilex.ai/products/limo-cobot)

---

### LIMO Überholt TurtleBot

In dieser Praktikumsaufgabe wird ein dynamisches Roboter-Interaktionsszenario zwischen dem LIMO Cobot und dem vorausfahrenden TurtleBot 4 umgesetzt. Der LIMO Cobot schätzt mittels Sensorik kontinuierlich die Geschwindigkeit des TurtleBots, berechnet eine Trajektorienprognose und führt bei gewähltem Abstand ein synchronisiertes Überholmanöver mit Wende- und Einscherphase durch.

**Genutzte Hardware:**
AgileX LIMO Cobot & TurtleBot 4
[![TurtleBot 4](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)](https://turtlebot.github.io/turtlebot4-user-manual/)
*Quelle / Bildnachweis:* [TurtleBot 4 User Manual (Clearpath Robotics / Open Robotics)](https://turtlebot.github.io/turtlebot4-user-manual/)

---

### Niryo Objektdetektion & Turmbau

Dieses Praktikum vereint Computer Vision, Deep Learning und kollaborative Robotik für eine Sortier- und Stapelaufgabe. Die Studierenden trainieren ein Convolutional Neural Network (CNN / Transfer Learning) zur Erkennung verschiedener Objektklassen mit dem Niryo Vision-Set, ermitteln Objekthöhen über eine Overhead RealSense D435 Tiefenbildkamera und bauen mit dem Niryo NED2 gestapelte Türme auf.

**Genutzte Hardware:**
Niryo NED2 & Intel RealSense D435
[![Niryo NED2](https://docs.niryo.com/robots/ned2/source/_static/img/ned2.png)](https://docs.niryo.com/robots/ned2/)
*Quelle / Bildnachweis:* [Niryo NED2 Offizielle Dokumentation](https://docs.niryo.com/robots/ned2/)

---

### TurtleBot Orientierungsschätzung (Kalman)

In dieser Aufgabe wird der TurtleBot 4 um einen externen Sensorknoten (Arduino Nicla Sense ME) mit 6-Achs-IMU und Magnetometer erweitert. Die Studierenden implementieren ein Kalman-Filter zur Echtzeit-Orientierungsschätzung (Gierwinkel / Quaternion) und vergleichen die Schätzergebnisse grafisch mit der internen TurtleBot-Odometrierelation.

**Genutzte Hardware:**
TurtleBot 4 & Arduino Nicla Sense ME
[![Arduino Nicla Sense ME](https://docs.arduino.cc/static/f509e51cce66aeecff4b9c1dcecb8cf5/39564/nicla-sense-me.jpg)](https://docs.arduino.cc/hardware/nicla-sense-me/)
*Quelle / Bildnachweis:* [Arduino Docs (Arduino S.r.l.)](https://docs.arduino.cc/hardware/nicla-sense-me/)

---

### TurtleBot Pfadplanung & SLAM

Dieses Praktikum beinhaltet die vollständige Navigationspipeline autonomer mobiler Roboter von der Kartierung bis zur Bewegungsplanung. Nach der Erstellung eines Occupancy Grids mit `slam_toolbox` diskretisieren die Studierenden den Raum als Suchgraph und implementieren sowie visualisieren Suchalgorithmen (Dijkstra und A*) im Vergleich zu ROS 2 Nav2.

**Genutzte Hardware:**
TurtleBot 4 (Mobiles Robotiksystem)
[![TurtleBot 4](https://turtlebot.github.io/turtlebot4-user-manual/media/TurtleBot4.jpg)](https://turtlebot.github.io/turtlebot4-user-manual/)
*Quelle / Bildnachweis:* [TurtleBot 4 User Manual (Clearpath Robotics / Open Robotics)](https://turtlebot.github.io/turtlebot4-user-manual/)
