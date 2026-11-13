"""
MoveIt 2 Python API (moveit_py) ile hareket planlama örneği.

ÖN KOŞUL: MoveIt Setup Assistant ile 'rrr_kol_moveit_config' paketi oluşturulmuş olmalı
(planlama grubu adı: "arm", uç: tool0, isimli poz: "hazir"). Adımlar konular/08-yazilim.md'de.

Bu betik tek başına `python` ile değil, MoveIt yapılandırmasını parametre olarak
aktaran bir launch dosyasıyla çalıştırılır (MoveIt "MoveItPy" eğitimindeki gibi).
Not: ROS 2 kurulu bir makinede test edilmemiştir; API, resmî MoveIt 2 eğitimini izler.
"""
import time
import rclpy
from rclpy.logging import get_logger
from moveit.planning import MoveItPy
from geometry_msgs.msg import PoseStamped


def planla_ve_yurut(robot, bilesen, logger):
    logger.info("Plan hesaplanıyor...")
    sonuc = bilesen.plan()
    if sonuc:
        logger.info("Plan bulundu, yürütülüyor.")
        robot.execute(sonuc.trajectory, controllers=[])
    else:
        logger.error("Plan bulunamadı!")
    time.sleep(1.0)


def main():
    rclpy.init()
    logger = get_logger("rrr_kol_moveit")
    robot = MoveItPy(node_name="rrr_kol_moveit_py")
    kol = robot.get_planning_component("arm")

    # 1) İsimli poza git (Setup Assistant'ta tanımlanan "hazir")
    kol.set_start_state_to_current_state()
    kol.set_goal_state(configuration_name="hazir")
    planla_ve_yurut(robot, kol, logger)

    # 2) Kartezyen hedef poza git (x–z düzleminde)
    hedef = PoseStamped()
    hedef.header.frame_id = "base_link"
    hedef.pose.position.x = 0.35
    hedef.pose.position.z = 0.08 + 0.25   # eklem1 yüksekliği + 0.25 m
    hedef.pose.orientation.w = 1.0
    kol.set_start_state_to_current_state()
    kol.set_goal_state(pose_stamped_msg=hedef, pose_link="tool0")
    planla_ve_yurut(robot, kol, logger)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
