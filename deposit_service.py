"""Логика для вычисления депозита."""

from datetime import date
from typing import Tuple, Dict, Any
from dateutil.relativedelta import relativedelta

from forms import DataForm


class DepositCalculator:
    """Класс для расчета депозита и валидации данных."""

    @staticmethod
    def get_datetime_after_n_months(old_date: date, number_of_months: int) -> date:
        """Возвращает дату через number_of_months месяцев.

        Args:
            old_date (date): Исходная дата.
            number_of_months (int): Количество месяцев для добавления.

        Returns:
            date: Новая дата через заданное количество месяцев.
        """
        new_date = old_date + relativedelta(months=number_of_months)
        return new_date.date()

    @staticmethod
    def calculate_next_month_rate(current_amount: float, rate: float) -> float:
        """Рассчитывает сумму следующего месяца на основе текущей суммы и ставки.

        Args:
            current_amount (float): Текущая сумма.
            rate (float): Процентная ставка.

        Returns:
            float: Новая сумма для следующего месяца.
        """
        return current_amount * (1 + rate / 12 / 100)

    @staticmethod
    def calculate_amount(
        initial_date: date, amount: float, periods: int, rate: float
    ) -> Dict[str, float]:
        """Вычисляет все предстоящие выплаты и их даты.

        Возвращает словарь, где ключ — дата выплаты, значение — сумма выплаты.

        Args:
            initial_date (date): Дата начала.
            amount (float): Начальная сумма.
            periods (int): Количество периодов (месяцев).
            rate (float): Процентная ставка.

        Returns:
            dict[str, float]: Словарь с датами и соответствующими суммами выплат.
        """
        result = {}
        current_date = initial_date
        current_amount = amount

        for i in range(1, periods + 1):
            current_amount = DepositCalculator.calculate_next_month_rate(
                current_amount=current_amount, rate=rate
            )
            current_date = DepositCalculator.get_datetime_after_n_months(
                old_date=initial_date, number_of_months=i - 1
            )
            result[str(current_date)] = round(current_amount, 2)

        return result

    @staticmethod
    def validate_deposit_data(data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Валидация данных для вычисления депозита.

        Args:
            data (dict): Входные данные.

        Returns:
            Tuple[bool, dict]: Кортеж, где первая переменная булева - результат валидации,
                               а вторая - валидированные данные или ошибки.
        """
        form = DataForm(data=data)
        if form.validate():
            return True, {
                "initial_date": form.date.data,
                "amount": form.amount.data,
                "periods": form.periods.data,
                "rate": form.rate.data,
            }
        return False, form.errors

    @staticmethod
    def process_deposit_request(data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        """Обрабатывает запрос.

        Args:
            data (dict): Входные данные запроса.

        Returns:
            Tuple[dict, int]: Кортеж с результатом (либо вычисленный результат, либо ошибки)
                              и соответствующим статусом.
        """
        is_valid, result = DepositCalculator.validate_deposit_data(data)

        if is_valid:
            calculated_data = DepositCalculator.calculate_amount(**result)
            return calculated_data, 200

        return {"errors": result}, 400
