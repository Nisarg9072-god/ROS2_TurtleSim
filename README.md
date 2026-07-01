# my_robot_controller

A ROS2 Python package containing basic robot controller nodes built with `rclpy`.

## Nodes

### `draw_circle_node`
Makes a TurtleSim turtle drive in a circle by publishing velocity commands to `/turtle1/cmd_vel`.

- **Linear velocity:** 2.0 m/s  
- **Angular velocity:** 1.0 rad/s  
- Publishes every 1 second

### `test_node` (my_first_node)
A simple starter node that logs a hello message every second using a timer callback.

## Dependencies

- ROS2 (tested on Humble/Jazzy)
- `rclpy`
- `geometry_msgs`
- `turtlesim`

## Build & Run

```bash
# From your ROS2 workspace root
colcon build --packages-select my_robot_controller
source install/setup.bash

# Run the draw circle node
ros2 run my_robot_controller draw_circle_node

# Run the first node
ros2 run my_robot_controller test_node
```

## Usage with TurtleSim

In separate terminals:

```bash
# Terminal 1 — launch turtlesim
ros2 run turtlesim turtlesim_node

# Terminal 2 — run the draw circle controller
ros2 run my_robot_controller draw_circle_node
```

## Author

Nisarg
