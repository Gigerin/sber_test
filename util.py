from datetime import date
from dateutil.relativedelta import relativedelta


def get_datetime_after_n_months(old_date: date, number_of_months: int) -> date:
    new_date = old_date + relativedelta(months=number_of_months)
    return new_date.date()


def calculate_next_month_rate(current_amount: int, rate: float) -> float:
    return current_amount * (1 + rate / 12 / 100)
