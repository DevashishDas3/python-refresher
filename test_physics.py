import unittest
import physics
import numpy as np

class PhysicsTest(unittest.TestCase):
    def test_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(3, 5), 147.15)
        self.assertNotEqual(physics.calculate_buoyancy(3, 5), 15)
        #self.assertEqual(physics.calculate_buoyancy(-2, -2), ValueError) -> test all of pos,0 and pos,neg combinations

    def test_floating(self):
        self.assertEqual(physics.will_it_float(50,2), True)
        self.assertNotEqual(physics.will_it_float(1000,3), False)
        self.assertEqual(physics.will_it_float(10009920,3), False)
        #self.assertEqual(physics.will_it_float(-3, -4), ValueError)

    def test_pressure(self):
        self.assertEqual(physics.calculate_pressure(3), 29430)
        self.assertNotEqual(physics.calculate_pressure(21), 206009)
        self.assertEqual(physics.calculate_pressure(21), 206010)
        #self.assertEqual(physics.calculate_pressure(-3), ValueError)

    def test_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(15,5), 3)
        self.assertNotEqual(physics.calculate_acceleration(15,3), 3.000001)
        self.assertEqual(physics.calculate_acceleration(6,3), 2)
    
    def test_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(10,5), 2)
        self.assertNotEqual(physics.calculate_angular_acceleration(10,5), 3)
        self.assertRaises(physics.calculate_angular_acceleration(-10,2), ValueError)
    
    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(-3, 30, -7), ValueError)
        self.assertNoteEqual(physics.calculate_torque(-3, 90, -7), -21)
        self.assertEqual(physics.calculate_torque(3,90,7), 21)
    
    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(5,5), 125)
        self.assertEqual(physics.calculate_moment_of_inertia(3,0), ValueError)
        self.assertEqual(physics.calculate_moment_of_inertia(-3,3), ValueError)
        self.assertNotEqual(physics.calculate_moment_of_inertia(-3,3), -27)
    
    def test_calculate_auv_acceleration(self):
        pass

    def test_calculate_auv_angular_acceleration(self):
        pass

    def test_calculate_auv2_acceleration(self):
        pass

    def test_calculate_auv2_angular_acceleration(self):
        pass

    def test_stimulate_auv2_motion(self):
        self.assertEqual(physics.stimulate_auv2_motion([30,40,90,100], np.pi/3, 4, 3))




if __name__ == "__main__":
    unittest.main()

