"Тестирование вспомогательных функций вычисления депозита"
from datetime import datetime
import pytest
from util import get_datetime_after_n_months, calculate_next_month_rate, calculate_amount


# Tests for get_datetime_after_n_months
def test_get_datetime_after_n_months_normal_case():
    "Стандартный тест"
    old_date = datetime(2022, 1, 15)
    number_of_months = 3
    expected_date = datetime(2022, 4, 15).date()
    assert get_datetime_after_n_months(old_date, number_of_months) == expected_date

def test_get_datetime_after_n_months_crossing_year_boundary():
    "Проверка при переходе в новый год"
    old_date = datetime(2022, 11, 30)
    number_of_months = 2
    expected_date = datetime(2023, 1, 30).date()
    assert get_datetime_after_n_months(old_date, number_of_months) == expected_date

def test_get_datetime_at_end_of_month():
    "Проверка при выпадении платежа на последнее число месяца"
    old_date = datetime(2024, 8, 31)
    number_of_months = 1
    expected_date = datetime(2024, 9, 30).date()
    assert get_datetime_after_n_months(old_date, number_of_months) == expected_date
def test_get_datetime_after_n_months_february_leap_year():
    "Проверка при високосном годе"
    old_date = datetime(2020, 1, 31)
    number_of_months = 1
    expected_date = datetime(2020, 2, 29).date()
    assert get_datetime_after_n_months(old_date, number_of_months) == expected_date


# Tests for calculate_next_month_rate
def test_calculate_next_month_rate_normal_case():
    "Стандартный тест"
    current_amount = 1000
    rate = 5.5
    expected_amount = 1004.58
    assert calculate_next_month_rate(current_amount, rate) == pytest.approx(expected_amount, 0.01)

def test_calculate_next_month_rate_zero_rate():
    "Нулевой rate"
    current_amount = 1000
    rate = 0
    expected_amount = 1000.00
    assert calculate_next_month_rate(current_amount, rate) == pytest.approx(expected_amount, 0.01)


# Tests for calculate_amount
def test_calculate_amount_normal_case():
    "Стандартный тест"
    initial_date = datetime(2022, 1, 15)
    amount = 1000
    periods = 3
    rate = 12
    expected_result = {
        '2022-01-15': 1010.0,
        '2022-02-15': 1020.1,
        '2022-03-15': 1030.3
    }
    assert calculate_amount(initial_date, amount, periods, rate) == expected_result

def test_calculate_amount():
    "Проверка вычисления при правильных входных данных"
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
