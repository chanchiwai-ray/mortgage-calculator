# Mortgage Calculator

Mortgage calculator provides a simple command line program to show the various
costs of buying a house. The formula used are based on the [Wikipedia][wikipedia]

## Installation

You can install the tool locally via `pip`:

```shell
pip install .
```

Or if you prefer installing it inside a virtual environment:

```shell
# Create virtual environment
python3 -m venv venv

# Source the virtual environment, and install the tool under the venv
source venv/bin/active
pip install .
```

## Usage

To calculate the mortgage summary, you can run

```shell
mortgage-calculator summary -v 5000000
```

To calculate the repayment for each month up to 3 years, you can run

```shell
mortgage-calculator breakdown -v 5000000 -y 3
```

For more information, you can run

```shell
mortgage-calculator -h
mortgage-calculator summary -h
mortgage-calculator breakdown -h
```

[wikipedia]: https://en.wikipedia.org/wiki/Mortgage_calculator
