import numpy as np

g0 = 9.80665
Isp = 300

def calculate_evasion_delta_v(obj, threat):
    direction = obj.r - threat.r
    direction = direction / np.linalg.norm(direction)
    delta_v = direction * 0.01
    return delta_v

def fuel_used(mass, delta_v):
    dv = np.linalg.norm(delta_v)
    return mass * (1 - np.exp(-dv / (Isp * g0)))