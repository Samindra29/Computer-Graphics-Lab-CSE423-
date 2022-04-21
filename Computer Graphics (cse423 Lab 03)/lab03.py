from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from random import *

def drawCircle(r, center_x, center_y):
    glBegin(GL_POINTS)
    glVertex2f(center_x, center_y)
    glEnd()


def midpoint_circle(r, center_x, center_y):
    # saving all the points
    slice_points = []

    # define
    x = 0
    y = r
    slice_points.append((x + center_x, y + center_y))

    # decision parameter d
    d = 1 - r

    while x < y - 1:
        if d >= 0:
            # choose lower pixel (SE)
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
            drawCircle(r, x, y)

        else:
            # choose upper pixel (E)
            d = d + 2 * x + 3
            x = x + 1
            drawCircle(r, x, y)

        slice_points.append((x + center_x, y + center_y))
        # print("\n--------")

    circle_points = get_other_points(slice_points)
    # print((circle_points))

    # print("\n---midpoint circle end---\n")
    return circle_points


def get_other_points(slice_points):
    circle_points_array = []
    zone0_array = []
    zone1_array = []
    zone2_array = []
    zone3_array = []
    zone4_array = []
    zone5_array = []
    zone6_array = []
    zone7_array = []

    for s in range(len(slice_points)):
        x, y = slice_points[s][0], slice_points[s][1]
        zone0_array.append((y, x))
        zone1_array.append((x, y))
        zone2_array.append((-x, y))
        zone3_array.append((-y, x))
        zone4_array.append((-y, -x))
        zone5_array.append((-x, -y))
        zone6_array.append((x, -y))
        zone7_array.append((y, -x))

    circle_points_array.append(zone0_array)
    circle_points_array.append(zone1_array)
    circle_points_array.append(zone2_array)
    circle_points_array.append(zone3_array)
    circle_points_array.append(zone4_array)
    circle_points_array.append(zone5_array)
    circle_points_array.append(zone6_array)
    circle_points_array.append(zone7_array)

    return circle_points_array


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    # call the draw methods here

    coordinates = midpoint_circle(500, 0, 0)
    for i in coordinates:
        for j in i:
            splitted = j.split(",")




    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Shundor circle patters :")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
