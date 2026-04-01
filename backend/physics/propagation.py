import numpy as np

mu = 398600.4418

def acceleration(r):
    return -mu * r / np.linalg.norm(r)**3

def update_position(obj, dt=1):
    a = acceleration(obj.r)
    obj.v += a * dt
    obj.r += obj.v * dt