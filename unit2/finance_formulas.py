
class Finance:
    """
    This is a class which implements several
    finance formulas using the TDD
    approach:
    """
    #  cash flow: Income - Expenses
    #  Net worth: Assets - debts
    #  Net income: Revenue - expenses

    def cash_flow(self, income, expenses):
        if income < 0:
            return
        return income - expenses

    def worth(self, assets, debts):
        return assets - debts

    def income(self, revenue, expenses):
        return revenue - expenses
