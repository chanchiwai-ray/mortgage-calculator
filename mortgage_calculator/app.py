"""Mortgage calculator command line interface."""

from typing import Union

import click
from rich.console import Console

from mortgage_calculator.table import (
    mortgage_payment_breakdown_table,
    mortgage_summary_table,
)

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


def validate_input(ctx: click.Context, param: str, value: Union[int, float]) -> Union[int, float]:  # noqa: ARG001
    """Validate the input to the command line interface."""
    if value < 0:
        raise click.BadParameter("must be a non-negative value")
    return value


@click.group(context_settings=CONTEXT_SETTINGS)
def cli() -> None:
    """Calculate various costs of buying a house."""


@cli.command()
@click.option(
    "-v",
    "--housing-value",
    required=True,
    callback=validate_input,
    show_default=True,
    help="The value of the house.",
    type=float,
)
@click.option(
    "-r",
    "--interest-rate",
    default=2.5,
    callback=validate_input,
    show_default=True,
    type=float,
    help="The annual interest rate in percentage.",
)
@click.option(
    "-p",
    "--loan-period",
    default=30,
    callback=validate_input,
    show_default=True,
    type=int,
    help="The loan period in years.",
)
@click.option(
    "-l",
    "--loan-to-value",
    default=90,
    callback=validate_input,
    show_default=True,
    type=float,
    help="The loan to value in percentage.",
)
def summary(
    housing_value: float,
    interest_rate: float,
    loan_period: int,
    loan_to_value: float,
) -> None:
    """Show the mortgage summary table."""
    console = Console()
    console.print(
        mortgage_summary_table(
            housing_value,
            interest_rate,
            loan_period,
            loan_to_value,
        ),
        justify="center",
    )


@cli.command()
@click.option(
    "-v",
    "--housing-value",
    required=True,
    callback=validate_input,
    show_default=True,
    help="The value of the house.",
    type=float,
)
@click.option(
    "-r",
    "--interest-rate",
    default=2.5,
    callback=validate_input,
    show_default=True,
    type=float,
    help="The annual interest rate in percentage.",
)
@click.option(
    "-p",
    "--loan-period",
    default=30,
    callback=validate_input,
    show_default=True,
    type=int,
    help="The loan period in years.",
)
@click.option(
    "-l",
    "--loan-to-value",
    default=90,
    callback=validate_input,
    show_default=True,
    type=float,
    help="The loan to value in percentage.",
)
@click.option(
    "-y",
    "--up-to-year",
    default=3,
    callback=validate_input,
    show_default=True,
    type=int,
    help="Limit the output up to certain year. ",
)
def breakdown(
    housing_value: float,
    interest_rate: float,
    loan_period: int,
    loan_to_value: float,
    up_to_year: int,
) -> None:
    """Show the mortgage payment breakdown table."""
    console = Console()
    console.print(
        mortgage_payment_breakdown_table(
            housing_value,
            interest_rate,
            loan_period,
            loan_to_value,
            int(up_to_year) if up_to_year <= loan_period else loan_period,
        ),
        justify="center",
    )


def main() -> None:
    """Entrypoint to the command line interface."""
    cli(obj={})


if __name__ == "__main__":
    main()
