"Main flask app"
from flask import Flask, request, jsonify
from forms import DataForm

from util import calculate_amount

app = Flask(__name__)


@app.route("/api/calculate_deposit", methods=["POST"])
def calculate_deposit():
    """
    Проверить входные данные и затем вычислить депозит.
    :return: dict[str, float] or 400
    """
    data = request.get_json()

    form = DataForm(data=data)

    if form.validate():
        data = calculate_amount(
            form.date.data, form.amount.data, form.periods.data, form.rate.data
        )
        return jsonify(data), 200
    return jsonify(errors=form.errors), 400


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
