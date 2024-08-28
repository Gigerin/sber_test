"""Main flask app"""

from flask import Flask, request, jsonify
from waitress import serve

from deposit_service import DepositCalculator

app = Flask(__name__)


@app.route("/api/calculate_deposit", methods=["POST"])
def calculate_deposit():
    """Handle для функции calculate_deposit

    Returns:
        dict[str, float]: Словарь с датой депозита и суммой депозита для каждого месяца
        Tuple: ответ с кодом 400 и описанием ошибки
    """
    data = request.get_json()
    response_data, status_code = DepositCalculator.process_deposit_request(data)
    return jsonify(response_data), status_code


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
