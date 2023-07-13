import math
import numpy

g = 9.81

#calculate the buoyancy given the volume of the object (v), the density of the fluid (density_fluid), and the gravitational constant (g = 9.81)
#formula -> Bf = pVg
def calculate_buoyancy(v,  density_fluid):
    if v < 0 or density_fluid < 0:
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