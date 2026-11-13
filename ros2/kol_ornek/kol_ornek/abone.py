"""Eklem açılarını dinler, düz kinematikle uç konumunu hesaplar ve yayınlar (Konu 2)."""
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PointStamped

L = (0.30, 0.25, 0.10)   # kod/robot_kol.py ile aynı uzuv boyları [m]


class UcHesaplayici(Node):
    def __init__(self):
        super().__init__("uc_hesaplayici")
        self.create_subscription(JointState, "ornek/eklem_durumu", self.geldi, 10)
        self.pub = self.create_publisher(PointStamped, "ornek/uc_konumu", 10)
        self.sayac = 0

    def geldi(self, msg: JointState):
        x = y = a = 0.0
        for Li, qi in zip(L, msg.position):
            a += qi
            x += Li * math.cos(a)
            y += Li * math.sin(a)
        out = PointStamped()
        out.header = msg.header
        out.header.frame_id = "base_link"
        out.point.x, out.point.y = x, y
        self.pub.publish(out)
        self.sayac += 1
        if self.sayac % 10 == 0:          # her saniye bir satır yaz
            q = ", ".join(f"{math.degrees(v):6.1f}" for v in msg.position)
            self.get_logger().info(f"q = ({q})°  →  uç = ({x:.3f}, {y:.3f}) m")


def main():
    rclpy.init()
    dugum = UcHesaplayici()
    try:
        rclpy.spin(dugum)
    except KeyboardInterrupt:
        pass
    finally:
        dugum.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()