# My solutions for Advent of Code 2021

![Python package](https://github.com/vmorris/aoc2021/workflows/Python%20package/badge.svg)

## Setup

After cloning this repository, create a virtual environment, activate it, and install.
```
$ cd aoc2021
aoc2021 $ python3 -m venv venv
aoc2021 $ . venv/bin/activate
(venv) aoc2021 $ pip install -e .[test]
```

## Run daily solutions

eg.
```
(venv) aoc2021 $ python aoc2021/day03/solution.py 
153
2421944712
```

## Test Suite
Run individual days with `pytest tests/test_day##.py`

Run the whole test suite with `pytest --cov=aoc2021`
