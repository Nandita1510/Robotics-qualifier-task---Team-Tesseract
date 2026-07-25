import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
from math import atan2, sin, cos


def create_pose(x, y, yaw):
    pose = PoseStamped()

    pose.header.frame_id = "map"

    pose.pose.position.x = x
    pose.pose.position.y = y

    # Convert yaw to quaternion
    pose.pose.orientation.z = sin(yaw / 2.0)
    pose.pose.orientation.w = cos(yaw / 2.0)

    return pose


def main():

    rclpy.init()

    navigator = BasicNavigator()

    print("Waiting for Nav2...")
    navigator.waitUntilNav2Active()

    navigator.clearAllCostmaps()

    print("Nav2 Ready!")

    # -----------------------------
    # Smooth Rectangle Waypoints
    # -----------------------------
    coords = [
        (-1.983951, -0.511981),
        (-1.489455, -0.514455),
        (-0.384785, -0.530502),
        (0.288360, -0.575950),
        (0.574379, -0.188141),
        (0.546342, 0.516840),
        (-0.568640, 0.575018),
        (-0.989907, 0.492966),
        (-1.757479, 0.591486),
        (-2.026140, -0.532810),
    ]

    # -----------------------------
    # Create waypoint poses
    # -----------------------------
    waypoints = []

    for i in range(len(coords)):

        x, y = coords[i]

        if i < len(coords) - 1:
            nx, ny = coords[i + 1]
        else:
            nx, ny = coords[0]     # Face first waypoint

        yaw = atan2(ny - y, nx - x)

        waypoints.append(create_pose(x, y, yaw))

    cycles = 3

    # -----------------------------
    # Run Mission
    # -----------------------------
    for cycle in range(cycles):

        print(f"\nCycle {cycle + 1} Started")

        navigator.followWaypoints(waypoints)

        while not navigator.isTaskComplete():
            rclpy.spin_once(navigator, timeout_sec=0.1)

        result = navigator.getResult()

        if result:
            print("✓ Loop Completed")
        else:
            print("✗ Mission Failed")
            break

    print("\nMission Completed")

    rclpy.shutdown()


if __name__ == "__main__":
    main()
    