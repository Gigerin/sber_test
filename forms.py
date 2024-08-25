" Формы для валидации входных данных"
from datetime import datetime

from wtforms import Form, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class DataForm(Form):
    "Форма для проверки данных для депозита"
    date = DateField("date", format="%d.%m.%Y", validators=[DataRequired()])
    periods = IntegerField(
        "periods", validators=[DataRequired(), NumberRange(min=1, max=60)]
    )
    amount = IntegerField(
        "amount", validators=[DataRequired(), NumberRange(min=10000, max=3000000)]
    )
    rate = FloatField(
        "rate", validators=[DataRequired(), NumberRange(min=1.0, max=8.0)]
    )

    def validate_date(self, field):
        "Метод для валидации и парсинга строки даты формата DD.MM.YYYY."
        try:
            field.data = datetime.strptime(field.data, "%d.%m.%Y")
        except ValueError as exc:
            raise ValidationError(
                "Invalid date format. Please use DD.MM.YYYY."
            ) from exc
