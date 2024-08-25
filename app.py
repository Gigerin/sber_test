from flask import Flask, request, jsonify
from forms import DataForm
from datetime import datetime
from dateutil.relativedelta import relativedelta

from util import get_datetime_after_n_months, calculate_next_month_rate, calculate_amount

app = Flask(__name__)



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
