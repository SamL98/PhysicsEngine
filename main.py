import cv2 as cv
import numpy as np
from time import sleep

from draw_util import clear
from draw import draw_shape
from line import create_line
from circle import create_ball

from gravity import calc_pos_and_vel
from collider import collide_inelastic

g = 10
w, h = 200, 400
kexit = 27

canvas = np.ones((h, w))
ball = create_ball(pos=[0, w//2-10])
line = create_line((h-2, 0), (h//4, w-1))

shapes = [ball, line]
def shdUpdate():
    for i in range(len(shapes)):
        if shapes[i].needsUpdate:
            return True
    return False

cv.namedWindow('canvas')

init_timestep = True
while(1):
    if init_timestep or shdUpdate():
        init_timestep = False

        clear(canvas)
        draw_shape(canvas, ball)
        draw_shape(canvas, line)
        collide_inelastic(ball, line)

        ay = sum(force.vec[0] for force in ball.forces)
        y, vy = calc_pos_and_vel(ball.bbox.center[0], ball.vel[0], a=ay, g=g, dt=0.125)

        ax= sum(force.vec[1] for force in ball.forces)
        x, vx = calc_pos_and_vel(ball.bbox.center[1], ball.vel[1], a=ax, g=0, dt=0.125)

        ball.setPos([y, x])
        ball.setVel([vy, vx])

    cv.imshow('canvas', canvas)

    k = cv.waitKey(20)
    if k == kexit:
        break

cv.destroyAllWindows()