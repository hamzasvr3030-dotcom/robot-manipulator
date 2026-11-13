"""Eklem açılarını 10 Hz ile yayınlar (sensor_msgs/JointState). Açılar yavaşça salınır."""
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class EklemYayinci(Node):
    def __init__(self):
        super().__init__("eklem_yayinci")
        self.declare_parameter("frekans_hz", 10.0)          # launch dosyasından değiştirilebilir
        hz = self.get_parameter("frekans_hz").value
        self.pub = self.create_publisher(JointState, "ornek/eklem_durumu", 10)
        self.t = 0.0
        self.dt = 1.0 / hz
        self.create_timer(self.dt, self.yayinla)
        self.get_logger().info(f"Yayın başladı: ornek/eklem_durumu ({hz:.0f} Hz)")

    def yayinla(self):
        self.t += self.dt
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ["joint1", "joint2", "joint3"]
        msg.position = [math.radians(30 + 20 * math.sin(0.5 * self.t)),   # omuz
                        math.radians(45 + 30 * math.sin(0.8 * self.t)),   # dirsek
                        math.radians(-30)]                                  # bilek sabit
        self.pub.publish(msg)


def main():
    rclpy.init()
    dugum = EklemYayinci()
    try:
        rclpy.spin(dugum)
    except KeyboardInterrupt:
        pass
    finally:
        dugum.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()