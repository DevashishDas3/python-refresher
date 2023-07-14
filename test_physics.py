import unittest
import physics

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
    
    def test_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(3,1), 3)


if __name__ == "__main__":
    unittest.main()

