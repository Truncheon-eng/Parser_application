from flask import Flask, request
from comparison_filter import comparision
app = Flask(__name__)
@app.route("/", methods=['POST'])
def main():
    # пришел запрос
    # выдираем из него query json
    request_data = request.get_json()
    print(request_data)
    data = comparision(request_data)
    # параметры (сформированный json) передаем в функцию (биржу)
    # когда ответ пришел возвращаем json (как написано ниже)
    return data

