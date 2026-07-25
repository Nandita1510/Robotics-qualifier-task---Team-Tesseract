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

## Software & Tools

- Ubuntu 22.04
- ROS 2 Humble
- TurtleBot3
- Gazebo
- RViz2
- Nav2 Navigation Stack

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
