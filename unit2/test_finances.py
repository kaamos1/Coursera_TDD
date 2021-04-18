
import unittest
from finance_formulas import Finance


#  cash flow: Income - Expenses
#  Net worth: Assets - debts
#  Net income: Revenue - expenses
#  Simple interest: I = p x r x  (p is principal, r is interest rate, and t is how long the money is borrowed in years)
#  Gains (or losses): (Market price - purchase price) / purchase price

class TestFinances(unittest.TestCase):
    def test_cash_flow(self):
        t1 = Finance()
        self.assertTrue(t1.cash_flow(10000, 5500), 4500)

    def test_net_worth(self):
        t1 = Finance()
        self.assertTrue(t1.worth(10000, 5500), 4500)

    def test_net_income(self):
        t1 = Finance()
        self.assertEqual(t1.income(10000, 5500), 4500)

    def test_simple_interest(self):
        t1 = Finance()
        self.assertEqual(t1.interest(1000, 3.5, 10), 0.0)  # TBD

    def test_gains_or_losses(self):
        pass


if __name__ == '__main__':
    unittest.main()
