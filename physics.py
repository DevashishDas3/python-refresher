import math
import numpy as np
import matplotlib.pyplot as plt

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
    if I < 0:
         raise ValueError
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    if F_magnitude <= 0 or r <= 0:
        raise ValueError
    F_direction = (F_direction * np.pi)/(180)
    return (r * F_magnitude * np.sin(F_direction))

def calculate_moment_of_inertia(m, r):
     if m < 0 or r <= 0:
          raise ValueError
     return ((m) * pow(r, 2))

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100):
     if mass < 0 or F_magnitude < 0:
          raise ValueError

     F_angle = (F_angle * 180)/(np.pi)

     force_x = (F_magnitude) * (np.cos(F_angle))
     force_y = (F_magnitude) * (np.sin(F_angle))

     total_force = np.array([
        force_x / mass,
        force_y / mass
     ])

     return total_force
     
def calculate_auv_angular_acceleration(F_magnitude, F_angle, thruster_distance = 0.5, inertia = 1):
     if thruster_distance < 0 or (F_magnitude < 0 or F_magnitude > 100) or inertia < 0:
          raise ValueError
     F_angle = (F_angle * 180)/(np.pi)
     AUV_torque = calculate_torque(F_magnitude, F_angle, thruster_distance)
     return (AUV_torque / inertia)

def calculate_auv2_acceleration(T, alpha, mass = 100):
     if mass < 0:
          raise ValueError
     alpha = (alpha * 180)/(np.pi)
     angular_mat = np.array([np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                            [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)])
     directional_forces = np.dot(angular_mat, T)
     total_acceleration = directional_forces / mass
     return total_acceleration
     

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia = 100):
     #add sin projection matrix 
     if L <= 0 or l<=0 or inertia < 0:
          raise ValueError
     r = np.sqrt(pow(L,2), pow(l,2))
     summation_torque = 0
     for i in range(len(T)):
          summation_torque += calculate_torque(T[i], alpha, r)
     return (summation_torque / inertia)

def simulate_auv2_motion(T, alpha, L, l, mass = 100, inertia = 100, dt = 0.1, t_final = 10, x0 = 0, y0 = 0, theta0 = 0):
     if L <= 0 or l<=0 or inertia < 0:
          raise ValueError
     r = np.sqrt(pow(L,2), pow(l,2))
     summation_torque = 0
     for i in range(len(T)):
          summation_torque += calculate_torque(T[i], alpha, r)
     angular_acceleration = summation_torque / inertia
     
     t = np.array([0])
     x = np.array([0])
     y = np.array([0])
     theta = np.array([0])
     v = np.array([0])
     omega = np.array([0])
     a = np.array([0])


     '''
     t = np.zeros_like(np.array([]))
     x = np.zeros_like(np.array([]))
     y = np.zeros_like(np.array([]))
     theta = np.zeros_like(np.array([]))
     v = np.zeros_like(np.array([]))
     omega = np.zeros_like(np.array([]))
     a = np.zeros_like(np.array([]))
     '''


     for i in range(len(T)):
          force_x = (T[i]) * (np.cos(alpha))
          force_y = (T[i]) * (np.sin(alpha))
          np.append(a, (force_x + force_y)/mass)

     for i in range(1, len(t_final)):
          angular_velocity = angular_acceleration * dt
          velocity = (a[i] - a[i-1]) * dt

          np.append(t, dt * i)
          np.append(omega, angular_velocity)
          np.append(v, velocity)

          displaced_x = x0 + (velocity * dt)
          displaced_y = y0 + (velocity *  dt)

          np.append(x, displaced_x)
          np.append(y, displaced_y)

          acceleration = (v[i] - v[i-1])/(dt)
          np.append(a, acceleration)

          dtheta = angular_velocity * dt

          np.append(theta, theta0 + dtheta  * i)

def plot_auv2_motion(t,x,a,y):
     plt.plot(t, x, label="x")
     plt.plot(t, y, label="y")
     plt.plot(t, a, label="Acceleration")
     plt.xlabel("Time (s)")
     plt.ylabel("Position (m), Velocity (m/s), Acceleration (m/s^2)")
     plt.legend()

     plt.show()
     #np.append(t, dt)


     





        


     
          
     
     
     