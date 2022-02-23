import robot_module as rm
import numpy as np
import math

"""By: Trey Castle"""


"""tests the functions from robot_module with the two planar link test case.
it then prints x y z and roll pitch yaw"""
def prob1():
    # length, twist, theta, d
    np.set_printoptions(precision=5, suppress=True)
    planar1 = rm.dh_transformation(1, 0, math.pi/2, 0)
    planar2 = rm.dh_transformation(1, 0, math.pi/2, 0)
    planar = rm.kinematic_chain([planar1, planar2])
    x, y, z = rm.get_pos(planar)
    roll, pitch, yaw = rm.get_rot(planar)
    print("Problem 2, part a:", x, y, z, roll, pitch, yaw)


"""tests the functions from robot_module with the UR5e test cases, with both the arm extended and shoulder
joint raised. it then prints x y z and roll pitch yaw for each."""
def prob2():
    # length, twist, theta, d
    np.set_printoptions(precision=5, suppress=True)
    list1 = [rm.dh_transformation(0, math.pi / 2, 0, 0.1625),
    rm.dh_transformation(-0.425, 0, 0, 0), rm.dh_transformation(-0.3922, 0, 0, 0),
    rm.dh_transformation(0, math.pi/2, 0, 0.1333), rm.dh_transformation(0, -math.pi/2, 0, 0.0997),
    rm.dh_transformation(0, 0, 0, 0.0996)]
    ur = rm.kinematic_chain(list1)
    x, y, z = rm.get_pos(ur)
    roll, pitch, yaw = rm.get_rot(ur)
    print("Problem 2, part b, case 1:", x, y, z, roll, pitch, yaw)
    list2 = [rm.dh_transformation(0, math.pi / 2, 0, 0.1625),
             rm.dh_transformation(-0.425, 0, -math.pi / 2, 0), rm.dh_transformation(-0.3922, 0, 0, 0),
             rm.dh_transformation(0, math.pi / 2, 0, 0.1333), rm.dh_transformation(0, -math.pi / 2, 0, 0.0997),
             rm.dh_transformation(0, 0, 0, 0.0996)]
    ur2 = rm.kinematic_chain(list2)
    x2, y2, z2 = rm.get_pos(ur2)
    roll2, pitch2, yaw2 = rm.get_rot(ur2)
    print("Problem 2, part b, case 2:", x2, y2, z2, roll2, pitch2, yaw2)


prob1()
prob2()
