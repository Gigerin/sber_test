"""Тестирование вспомогательных функций вычисления депозита"""

from datetime import datetime
import pytest
from deposit_service import DepositCalculator


class TestGetDatetimeAfterNMonths:
    "Тестирование функции get_datetime_after_n_months"

    @pytest.mark.parametrize(
        "old_date, number_of_months, expected_date",
        [
            (datetime(2022, 1, 15), 3, datetime(2022, 4, 15).date()),
            (datetime(2022, 11, 30), 2, datetime(2023, 1, 30).date()),
            (datetime(2024, 8, 31), 1, datetime(2024, 9, 30).date()),
            (datetime(2020, 1, 31), 1, datetime(2020, 2, 29).date()),
        ],
    )
    def test_get_datetime_after_n_months(
        self, old_date, number_of_months, expected_date
    ):
        "Параметризованный тест для get_datetime_after_n_months"
        assert (
            DepositCalculator.get_datetime_after_n_months(
                old_date=old_date, number_of_months=number_of_months
            )
            == expected_date
        )


class TestCalculateNextMonthRate:
    "Тестирование функции calculate_next_month_rate"

    def test_normal_case(self):
        "Стандартный тест"
        current_amount = 1000
        rate = 5.5
        expected_amount = 1004.58
        assert DepositCalculator.calculate_next_month_rate(
            current_amount=current_amount, rate=rate
        ) == pytest.approx(expected_amount, 0.01)


class TestCalculateAmount:
    "Тестирование функции calculate_amount"

    def test_case_with_correct_input(self):
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

        result = DepositCalculator.calculate_amount(
            initial_date=start_date, amount=amount, periods=periods, rate=rate
        )

        assert result == expected_result
