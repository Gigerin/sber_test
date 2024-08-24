from flask import Flask, request, jsonify
from forms import DataForm
from datetime import datetime
from dateutil.relativedelta import relativedelta

from util import get_datetime_after_n_months, calculate_next_month_rate

app = Flask(__name__)


def calculate_amount(date, amount, periods, rate):
    result = {}
    current_date = date
    current_amount = amount
    for i in range(1, periods + 1):

        current_amount = calculate_next_month_rate(
            current_amount, rate
        )
        current_date = get_datetime_after_n_months(date, i - 1)

        result[str(current_date)] = round(current_amount, 2)
    return result


@app.route("/api/calculate_deposit", methods=["POST"])
def calculate_deposit():
    data = request.get_json()

    form = DataForm(data=data)

    if form.validate():
        data = calculate_amount(
            form.date.data, form.amount.data, form.periods.data, form.rate.data
        )
        return jsonify(data), 200
    else:
        return jsonify(errors=form.errors), 400


if __name__ == "__main__":
    app.run(debug=True)
