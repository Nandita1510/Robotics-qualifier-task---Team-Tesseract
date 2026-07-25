# Track A — Robotics Qualifier: TurtleBot3 Navigation (ROS 2 + Nav2)

Implements both qualifier tasks:

- **Task 1 — ROS2 Setup & TurtleBot Navigation**: point-to-point navigation
  to user-defined goals using the Nav2 stack.
- **Task 2 — Repeated Waypoint Navigation**: loops the robot through a
  10-point waypoint circuit continuously (or for N cycles) without manual
  intervention.

## Meets Evaluation Criteria

- ✅ Simulation launches successfully (`bringup_sim.launch.py`)
- ✅ Robot navigates to ≥2 user-defined goals (`goal_navigation.py`)
- ✅ Continuous waypoint loop with stable localization (`waypoint_navigation.py`)

## Simulation World

This project uses the stock TurtleBot3 Gazebo world (`turtlebot3_world.launch.py`,
shipped with `turtlebot3_simulations`) — no custom `.world`/`.sdf` file is
included in this repo. Waypoint coordinates in `waypoint_navigation.py` are
tuned specifically for this world's free space.

## Requirements

- Ubuntu 22.04 (or a Docker container running Ubuntu 22.04, if your host
  OS is newer — e.g. Ubuntu 24.04)
- ROS 2 Humble
- Gazebo (classic) + `turtlebot3`, `turtlebot3_simulations`,
  `turtlebot3_navigation2`, `nav2_bringup`, `nav2_simple_commander`

Install the TurtleBot3 + Nav2 dependencies if not already present:

```bash
sudo apt update
sudo apt install -y \
  ros-humble-turtlebot3 \
  ros-humble-turtlebot3-simulations \
  ros-humble-turtlebot3-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-nav2-simple-commander
```


# Task 1 – Goal-Based Navigation using Nav2

## Overview

This project demonstrates goal-based autonomous navigation of a TurtleBot3 robot using the ROS 2 Navigation Stack (Nav2). The robot operates in a Gazebo simulation environment while RViz is used to set navigation goals and visualize the robot's movement.

---

## Objective

- Launch TurtleBot3 in Gazebo.
- Configure and start the Nav2 Navigation Stack.
- Visualize the robot in RViz.
- Navigate the robot to a user-defined goal.

---



---

## Workflow

1. Launch the TurtleBot3 simulation in Gazebo.
2. Start the Nav2 Navigation Stack.
3. Open RViz.
4. Set the robot's initial pose.
5. Select a destination using the **"2D Goal Pose"** tool in RViz.
6. Nav2 computes an optimal path and autonomously navigates the robot to the selected goal while avoiding obstacles.

---

## Project Structure

```
Robotics-qualifier-task-Team-Tesseract/
│
├── README.md
├── screenshots/
    ├── gazebo.png
    └── rviz.png

```

---

## Result

The TurtleBot3 successfully reached the user-selected goal using the ROS 2 Navigation Stack (Nav2).


# Task 2 – Autonomous Waypoint Navigation

## Overview

This task demonstrates autonomous waypoint navigation using TurtleBot3 in a Gazebo simulation with the ROS2 Nav2 Navigation Stack. The robot navigates through a predefined sequence of waypoints using the Nav2 Simple Commander API.

## Features

- TurtleBot3 simulation in Gazebo
- Autonomous navigation using Nav2
- Sequential waypoint traversal
- Goal status monitoring
- ROS2 Humble compatible

## Project Structure
~~~
Task2/
├── my_robot_controller                
|   ├── waypoint_navigation.py
|   ├── __init__.py
├── setup.py
├── package.xml
├── setup.cfg
├── resource 
└── test
~~~
## How to Run

1. Launch the TurtleBot3 Gazebo simulation.
2. Launch the Nav2 navigation stack.
3. Set the robot's initial pose in RViz.
4. Run the waypoint navigation node.
5. The robot will automatically visit all predefined waypoints.

## Output

The robot successfully navigates to each waypoint while avoiding obstacles using the Nav2 navigation framework.

---

## Notes

- The waypoint coordinates in `waypoint_navigation.py` are tuned for the
  free space in the stock `turtlebot3_world` Gazebo world. If you swap
  worlds, update `WAYPOINTS` accordingly.
- Tested with `TURTLEBOT3_MODEL=burger`.
