import cv2 as cv
import numpy as np
from time import sleep

from draw_util import clear
from draw import draw_shape
from line import create_line
from circle import create_ball

from collider import collide_inelastic

g = 9.8
w, h = 250, 500
kexit = 27

canvas = np.ones((h, w))

ball = create_ball(pos=[0, w//2-10])
ball.a = [g, 0]
ball.mass = 10.0

#line = create_line((h-2, 0), (h//2, w-1))
line = create_line((h//2, 0), (h-2, w-1))
line.restitution = 10.0

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

        for shape in shapes:
            shape.nextPos()

    cv.imshow('canvas', canvas)

    k = cv.waitKey(20)
    if k == kexit:
        break

cv.destroyAllWindows()