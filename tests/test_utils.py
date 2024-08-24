import pytest
from datetime import datetime
from app import calculate_amount


def test_calculate_amount():
    start_date = datetime(2021, 1, 31)
    amount = 10000
    periods = 7
    rate = 6.0

    expected_result = {
        "2021-01-31": 10050.0,
        "2021-02-28": 10100.25,
        "2021-03-31": 10150.75,
        "2021-04-30": 10201.51,
        "2021-05-31": 10252.51,
        "2021-06-30": 10303.78,
        "2021-07-31": 10355.29,
    }

    result = calculate_amount(start_date, amount, periods, rate)

    assert result == expected_result


def test_calculate_amount_with_large_periods():
    start_date = datetime(2024, 1, 1)
    amount = 10000
    periods = 60
    rate = 5.0

    result = calculate_amount(start_date, amount, periods, rate)

    assert len(result) == periods
    assert result["2024-01-01"] == 10041.67
    assert result["2028-12-01"] > amount


def test_calculate_amount_with_zero_rate():
    start_date = datetime(2024, 1, 1)
    amount = 10000
    periods = 12
    rate = 0.0

    result = calculate_amount(start_date, amount, periods, rate)

    assert all(v == amount for v in result.values())
