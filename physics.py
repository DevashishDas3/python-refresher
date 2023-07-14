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
            raise ValueError(f'Density input as {depth} is invalid')
    return (1000 * g * depth)

def calculate_acceleration(F, m):
    return F/m

def  calculate_angular_acceleration(tau, I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    l_small = (np.sin(F_direction) * r)
    l_large = (np.cos(F_direction) * r)
    return (F_magnitude) * (np.sin(F_direction)*(l_large)) * (np.cos(F_direction) *  l_small)
    #calculate F using magnitude  and direction
    '''
    if F_direction > 180 or (F_direction < 0 and F_direction > -180):
         return -1 * r * F_magnitude
    if F_direction > 360:
         raise ValueError("Angle must be between 0 and 360 degrees")
    return r * F_magnitude
    '''

def calculate_moment_of_inertia(m, r):
     return ((m) * pow(r, 2))

def calculate_auv_acceleration(F_magnitude, F_angle):
     pass
     
def calculate_auv_angular_acceleration(F_magnitude, F_angle):
     return (calculate_torque(F_magnitude, F_angle, 0.5) / calculate_moment_of_inertia(100, 0.5))

def calculate_auv2_acceleration(T, alpha):
     acceleration_resultant = np.array([])
     for i in T:
        np.append(acceleration_resultant, T/100)

def calculate_auv2_angular_acceleration(T, alpha, L, l, intertia, theta):
     inertia = 100
     angular_acceleration_resultant = np.array([])
     for i in range (len(T)):
        b = np.arctan(l/L)
        r = (L) / (np.cos(b))
        torque = calculate_torque(T[i], theta, r)
        angular_acceleration_resultant.append(torque/inertia)
    return angular

        


     
          
     
     
     