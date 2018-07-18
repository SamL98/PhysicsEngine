""" Functions for adding gravity to Shape objects """

"""
Using the kinematic equations, calculate the new position and
velocity given an initial position and velocity.

:param x: the y position of the object
:param v: the y velocity of the object
:param g: gravitational constant. default 10
:param a: any acceleration caused by external forces
:param dt: interval of time elapsed form last calculation
"""
def calc_pos_and_vel(x, v, g=10, a=0, dt=0.5):
    x += v*dt + .5*(g+a)*dt**2
    v += (g+a)*dt
    return x, v