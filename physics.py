import math
import numpy as np

g = 9.81

#calculate the buoyancy given the volume of the object (v), the density of the fluid (density_fluid), and the gravitational constant (g = 9.81)
#formula -> Bf = pVg
def calculate_buoyancy(v,  density_fluid):
    if v <= 0 or density_fluid <= 0:
            raise ValueError(f'Fluid density input as {density_fluid} with object volume {v} is invalid')
    return v * density_fluid * g

#compare density of the object with the density of the water
#if density is less than the  waters, the  object will float else it will sink
def will_it_float(mass, v):
    density_object = mass/v
    if density_object < 1000:
        if mass < 0 or v < 0:
            raise ValueError(f'Density input as {density_object} is invalid')
        return True
    else:
        return False
    
#pressure is calculated with the formula pgh, where p is (1000 water density), g is 9.81, and h is the depth
def calculate_pressure(depth):
    #depth = abs(depth)
    if depth < 0:
            raise ValueError(f'Depth input as {depth} is invalid')
    return (1000 * g * depth)

def calculate_acceleration(F, m):
    return F/m

def  calculate_angular_acceleration(tau, I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    F_direction = (F_direction * np.pi)/(180)
    return (r * F_magnitude * np.sin(F_direction))

def calculate_moment_of_inertia(m, r):
     return ((m) * pow(r, 2))

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100):
     F_angle = (F_angle * np.pi)/(180)
     total_force = (F_magnitude) * (np.cos(F_angle)) + (F_magnitude) * (np.sin(F_angle))
     return (total_force / mass)
     
def calculate_auv_angular_acceleration(F_magnitude, F_angle, thruster_distance = 0.5, inertia = 1):
     AUV_torque = calculate_torque(F_magnitude, F_angle, thruster_distance)
     return (AUV_torque / inertia)

def calculate_auv2_acceleration(T, alpha, mass = 100):
     alpha = (alpha * np.pi)/(180)
     angular_mat = np.array([np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                            [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)])
     directional_forces = np.dot(angular_mat, T)
     total_force = directional_forces[0,0] + directional_forces[1,0]
     return total_force / mass
     

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia = 100):
     r = np.sqrt(pow(L,2), pow(l,2))
     summation_torque = 0
     for i in range(len(T)):
          summation_torque += calculate_torque(T[i], alpha, r)
     return (summation_torque / inertia)




        


     
          
     
     
     