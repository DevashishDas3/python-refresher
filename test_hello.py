import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "hey")

    def test_add(self):
        self.assertEqual(hello.add(0,1), 1)
        self.assertNotEqual(hello.add(2,6), 7)
    
    def test_sub(self):
        self.assertEqual(hello.sub(0,1), -1)
        self.assertNotEqual(hello.sub(2,6), -2)
    
    def test_mul(self):
        self.assertEqual(hello.mul(3,5), 15)
        self.assertNotEqual(hello.mul(2,6), 14)
    
    def test_div(self):
        self.assertEqual(hello.div(0,1), 0)
        self.assertNotEqual(hello.div(6,2), 4.33)
    
    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)
        self.assertNotEqual(hello.sqrt(9), 3.1)
    
    def test_power(self):
        self.assertEqual(hello.power(2,3), 8)
        self.assertNotEqual(hello.power(2,2), 7)
    
    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertNotEqual(hello.log(10), 3)
    
    def test_exp(self):
        self.assertEqual(hello.exp(0), 1)
        self.assertEqual(hello.exp(1), 2.7182818284590452)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
