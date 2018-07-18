""" Implementation of inelastic and elastic collisions between objects """

import numpy as np

from circle import Circle
from line import Line
from force import Force

def _collide_cl(c, l, el=False):
    if l.m == np.inf:
        left_and_right = c.bbox.center[1] < l.bbox.l and c.bbox.r >= l.bbox.l
        right_and_left = c.bbox.center[1] > l.bbox.l and c.bbox.r <= l.bbox.r
        if left_and_right or right_and_left:
            if el:
                pass
            else:
                c.setVel([c.vel[0], 0])

    elif l.m == 0:
        under_and_above = c.bbox.center[0] > l.bbox.t and c.bbox.t <= l.bbox.t
        above_and_under = c.bbox.center[0] < l.bbox.t and c.bbox.b >= l.bbox.t
        if  under_and_above or above_and_under:
            if el:
                pass
            else:
                c.setVel([0, c.vel[1]])
                if not c.hasForceFrom(l):
                    mag = -10
                    if under_and_above:
                        mag = 10
                    c.addForce(Force([mag, 0], l))
                    
    else:
        if l.m > 0:
            theta = np.arctan(l.m)

            cnt = c.bbox.center
            above = cnt[0] < l.m*cnt[0] + l.b

            u, v = cnt[0], cnt[1]
            if above:
                theta -= np.pi/2.
                u += np.cos(theta)*c.rad
                v -= np.sin(theta)*c.rad
            else:
                theta += np.pi/2.
                u += np.sin(theta)*c.rad
                v += np.cos(theta)*c.rad

            x = -1. * (v - l.b)/l.m
            if (above and u >= x) or ((not above) and u <= x):
                c.setVel([0, c.vel[1]])
                if not c.hasForceFrom(l):
                    mag = -10
                    if above:
                        mag = 10

                    theta = np.arctan(l.m)
                    fx = -mag * np.sin(theta) * np.cos(theta)
                    fy = mag * np.cos(theta)**2
                    #print(mag*np.sin(theta), mag*np.cos(theta))
                    print(fx, fy)
                    #c.addForce(Force([0, -mag*np.cos(theta)], l))
                    c.addForce(Force([fy, fx], l))
        else:
            pass

def collide_inelastic(s1, s2):
    if type(s1) == Circle:
        if type(s2) == Line:
            _collide_cl(s1, s2, el=False)
    elif type(s2) == Circle:
        if type(s1) == Line:
            _collide_cl(s2, s1, el=False)