import numpy as np
import math

"""By: Trey Castle"""

"""takes in denavit-Hartenberg parameters and sets up a 4 x 4 array,
returning a combined homogenius transformation."""
def dh_transformation(length, twist, theta, d):
    trans = np.array(
            [[math.cos(theta), -math.sin(theta)*math.cos(twist), math.sin(theta)*math.sin(twist), length*math.cos(theta)],
             [math.sin(theta), math.cos(theta)*math.cos(twist), -math.cos(theta)*math.sin(twist), length*math.sin(theta)],
             [0, math.sin(twist), math.cos(twist), d],
             [0, 0, 0, 1]])
    return trans


"""recieves a list of transformation matrixes. It sets an identity matrix, then
uses a for loop to right multiply the content of the list together.
returns the total transformation."""
def kinematic_chain(list1):
    #input is assumed to be an array containing several dh transformation matrixes
    #list of matrixes
    trans = np.identity(4)
    for dh in list1:
        trans = np.matmul(trans, dh)
    return trans


"""receives a matrix and gets the slot corresponding to the x, y, & z locations"""
def get_pos(matrix):
    x = matrix[0, 3]
    y = matrix[1, 3]
    z = matrix[2, 3]
    return x, y, z


"""recieves a homogenius tranformation matrix as input.
it takes the slots from the matrix to calculate the roll pitch and yaw for rotation using inverse tangent2."""
def get_rot(homo):
    #change from atan to atan2
    roll = math.atan2(homo[2, 1], homo[2, 2])
    pitch = math.atan2(-homo[2, 0], (math.sqrt(homo[2, 1] + homo[2, 2])))
    yaw = math.atan2(homo[1, 0], homo[0, 0])
    return roll, pitch, yaw
