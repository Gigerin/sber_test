"Вспомогательные функции"
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def get_datetime_after_n_months(old_date: date, number_of_months: int) -> datetime:
    """
    Возвращает дату через number_of_months месяцев
    :param old_date:
    :param number_of_months:
    :return:
    """
    new_date = old_date + relativedelta(months=number_of_months)
    return new_date.date()


def calculate_next_month_rate(current_amount: int, rate: float) -> float:
    "Расчитывает amount следующего месяца на основе текущего и rate"
    return current_amount * (1 + rate / 12 / 100)


def calculate_amount(
    initial_date: date, amount: int, periods: int, rate: float
) -> dict[str, float]:
    """
    Вычисляет все предстоящие выплаты и их даты. Возвращает словарь вида "дата":число.
    :param initial_date:
    :param amount:
    :param periods:
    :param rate:
    :return:
    """
    result = {}
    current_date = initial_date
    current_amount = amount
    for i in range(1, periods + 1):

        current_amount = calculate_next_month_rate(current_amount, rate)
        current_date = get_datetime_after_n_months(initial_date, i - 1)

        result[str(current_date)] = round(current_amount, 2)
    return result
