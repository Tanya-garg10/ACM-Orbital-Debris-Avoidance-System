import numpy as np

def check_collision(obj1, obj2):
    dist = np.linalg.norm(obj1.r - obj2.r)
    return dist < 0.1