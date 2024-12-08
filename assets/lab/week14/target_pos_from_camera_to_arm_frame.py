import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from scipy.spatial.transform import Rotation as scipyR
import numpy as np

class FrameListener(Node):

    def __init__(self):
        super().__init__('homogeneous_transform')

        # Declare and acquire `target_frame` and `source_frame` parameter
        self.base_frame = self.declare_parameter('arm_base_frame', 'px100/base_link').get_parameter_value().string_value
        self.camera_frame = self.declare_parameter('camera_frame', 'camera_color_frame').get_parameter_value().string_value

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Call on_timer function every second
        self.timer = self.create_timer(1.0, self.on_timer)

        # CHANGE THIS! substitute `target_pos_wrt_camera_frame` with the position you get from aruco recognition node
        target_pos_wrt_camera_frame = np.array([0.038, -0.032, -0.28]) 
        # target_pos_wrt_camera_frame = np.array([0., 0., 0.]) 

        self.target_pos_wrt_camera_frame_tilde = np.concatenate(( target_pos_wrt_camera_frame, [1]))


    def on_timer(self):
        """ Get transformed position in arm base frame """
        t = self.tf_buffer.lookup_transform(
                self.base_frame,
                self.camera_frame,
                rclpy.time.Time())
        camera_frame_pos_msg = t.transform.translation
        camera_frame_rot_msg = t.transform.rotation
        camera_frame_quat = np.array([ camera_frame_rot_msg.x, camera_frame_rot_msg.y, camera_frame_rot_msg.z, camera_frame_rot_msg.w ])
        camera_frame_pos = np.array([ camera_frame_pos_msg.x, camera_frame_pos_msg.y, camera_frame_pos_msg.z ])
        # Rotation matrix
        R = scipyR.from_quat(camera_frame_quat).as_matrix()
        # Construct the corresponding homogeneous transformation matrix
        T = np.eye(4)  # Initialize homogeneous transformation matrix
        T[0:3, 0:3] = R
        T[0:3, 3] = camera_frame_pos
        T[3, 3] = 1.
        # Compute the transformed target position wrt arm base frame 
        target_pos_wrt_arm_frame = T @ self.target_pos_wrt_camera_frame_tilde

        self.get_logger().info('target_pos_wrt_arm_frame: {}'.format(target_pos_wrt_arm_frame[:3]))

def main():
    rclpy.init()
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == "__main__":
    main()

