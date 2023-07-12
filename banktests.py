import unittest
import bankaccount

class TestBank(unittest.TestCase):
    def tests(self):
        acc1 = bankaccount.Account("Dev", 123, 51.25)
        acc1.withdraw(10)
        self.assertAlmostEqual(acc1.display_balance(), "41.25")
        self.assertNotEqual(acc1.withdraw(2000), -1948.75)