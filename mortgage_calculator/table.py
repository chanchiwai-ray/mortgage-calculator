"""Mortgage calculator command line interface."""

from rich.table import Table

from mortgage_calculator.math import MortgageCalculator


def _to_currency_string(value: float) -> str:
    """Convert a float value to a currency string."""
    return f"$ {value:,.0f}"


def mortgage_summary_table(
    housing_price: float,
    interest_rate: float,
    loan_period: float,
    loan_to_value: float,
) -> Table:
    """Return the mortgage summary table."""
    table = Table(
        title="\n樓宇按揭總結\n(Mortgage Summary)\n",
        title_style="bold magenta",
        caption=(
            "\n未包含額外成本: 傭金，差餉，印花稅，管理費， 裝修費，等等..."
            "\n(Additional costs are not included: "
            "agency fee, rates, stamp duty, management fee, renovation fee, and etc...) \n"
        ),
        caption_style="grey37",
    )

    table.add_column("利率\n(Interest Rate)", justify="center")
    table.add_column("月供\n(Monthly Payment)", justify="center")
    table.add_column("首期\n(Down Payment)", justify="center")
    table.add_column("貸款額\n(Loan Amount)", justify="center")
    table.add_column("總利息\n(Total Interest)", justify="center")
    table.add_column("總置業成本\n(Total Cost)", justify="center")

    step_sizes = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
    for step in step_sizes:
        r = interest_rate + step
        mc = MortgageCalculator(housing_price, r, loan_period, loan_to_value)
        table.add_row(
            f"{r:.3f} %",
            _to_currency_string(mc.get_monthly_payment()),
            _to_currency_string(mc.get_down_payment()),
            _to_currency_string(mc.get_loan_amount()),
            _to_currency_string(mc.get_total_interest()),
            _to_currency_string(mc.get_total_cost()),
            style="bold red" if r == interest_rate else "",
        )

    return table


def mortgage_payment_breakdown_table(
    housing_price: float,
    interest_rate: float,
    loan_period: float,
    loan_to_value: float,
    up_to_year: int = 3,
) -> Table:
    """Return the mortgage payment breakdown table."""
    table = Table(
        title="\n每月還款\n(Monthly Payment Breakdown)\n",
        title_style="bold magenta",
        caption=(f"\n只展示到{up_to_year}年 " f"\n(Only show up to {up_to_year} year)\n"),
        caption_style="grey37",
    )

    table.add_column("期數\n(Month)", justify="center")
    table.add_column("利息\n(Interest)", justify="center")
    table.add_column("本金\n(Principal)", justify="center")
    table.add_column("月供\n(Monthly Payment)", justify="center")
    table.add_column("剩余貸款額\n(Remaining Loan Amount)", justify="center")

    mc = MortgageCalculator(housing_price, interest_rate, loan_period, loan_to_value)
    interests, principals, remaining_loans = mc.get_monthly_payment_breakdown()
    for i in range(int(up_to_year * 12 + 1)):
        index = f"{i} {f'({i//12} 年)' if i % 12 == 0 else ''}"
        table.add_row(
            index,
            _to_currency_string(interests[i]),
            _to_currency_string(principals[i]),
            _to_currency_string(interests[i] + principals[i]),
            _to_currency_string(remaining_loans[i]),
        )

    return table
