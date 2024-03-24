"""Mortgage calculator's core math module."""


class MortgageCalculator:
    """A mortgage calculator helper class."""

    def __init__(
        self,
        housing_price: float,
        interest_rate: float,
        loan_period: float,
        loan_to_value: float,
    ):
        """Initialize the calculator."""
        self.housing_price = housing_price
        self.loan_to_value = loan_to_value / 100
        self.loan_period = loan_period * 12  # load period in month
        self.interest_rate = interest_rate / 12 / 100  # interest rate in month

    def get_total_cost(self) -> float:
        """Get the total cost buying out a housing."""
        total_interest = self.get_total_interest()
        return self.housing_price + total_interest

    def get_loan_amount(self) -> float:
        """Get the loan amount."""
        return self.housing_price * self.loan_to_value

    def get_down_payment(self) -> float:
        """Get the down payment amount."""
        return self.housing_price * (1 - self.loan_to_value)

    def get_total_interest(self) -> float:
        """Get the total interest paid after buyting out a house."""
        p = self.get_loan_amount()
        c = self.get_monthly_payment()
        n = self.loan_period
        return c * n - p

    def get_monthly_payment(self) -> float:
        """Get the monthly payment to the bank."""
        n = self.loan_period
        r = self.interest_rate
        p = self.get_loan_amount()
        if r == 0:
            return p / n
        return p * r * (1 + r) ** n / ((1 + r) ** n - 1)

    def get_monthly_payment_breakdown(self) -> tuple[list[float], list[float], list[float]]:
        """Get the breakdowns of monthly payment into interest and principal payment."""
        n = self.loan_period  # load period in month
        r = self.interest_rate  # interest rate in month

        interest = 0.0
        principal = 0.0
        remaining_loan = self.get_loan_amount()
        monthly_repayment = self.get_monthly_payment()

        interests = [interest]
        principals = [principal]
        remaining_loans = [remaining_loan]
        for _ in range(int(n)):
            interest = remaining_loan * r
            principal = monthly_repayment - interest
            remaining_loan += interest - monthly_repayment
            interests.append(interest)
            principals.append(principal)
            remaining_loans.append(remaining_loan)
        return interests, principals, remaining_loans
