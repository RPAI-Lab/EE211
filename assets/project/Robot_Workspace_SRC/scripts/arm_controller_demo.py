import rclpy
from rclpy.node import Node
from interbotix_xs_msgs.msg import JointSingleCommand,JointGroupCommand
from sensor_msgs.msg import JointState


class ArmController(Node):
    def __init__(self):
        super().__init__("ArmController")
        self.arm_cmd_pub = self.create_publisher(JointSingleCommand, "/px100/commands/joint_single", 10)
        self.arm_group_pub = self.create_publisher(JointGroupCommand, "/px100/commands/joint_group", 10)
        self.arm_timer_pub = self.create_timer(0.1, self.timer_cb)
        self.joint_states_sub = self.create_subscription(JointState, "/joint_states", self.joint_states_cb, 10)
        #  /joint_states has the following joint info
        #  - waist
        #  - shoulder
        #  - elbow
        #  - wrist_angle
        #  - gripper
        #  - left_finger
        #  - right_finger

        #  self.arm_command = JointSingleCommand()
        self.arm_group_command = JointGroupCommand()
        self.arm_group_command.name = "arm"
        self.arm_group_command.cmd = [0.0, -0.3, 0.8, 1.0]

        self._joint_pos = []
        self._cnt = 0


    def joint_states_cb(self, msg):
        # print(msg.name)
        if len(msg.name) == 7:
            self._joint_pos.clear()
            for i in range(4):
                self._joint_pos.append(msg.position[i])

    def timer_cb(self):
        self.arm_group_pub.publish(self.arm_group_command)
        self._cnt += 1

        if self._cnt % 10 == 0:
            if len(self._joint_pos) == 4:
                print(self._joint_pos)

def main():
    rclpy.init(args=None)
    contoller = ArmController()
    rclpy.spin(contoller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
