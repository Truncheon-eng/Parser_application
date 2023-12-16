from flask import Flask, request
from comparison_filter import comparision
from find_things import final_output
app = Flask(__name__)
@app.route("/", methods=['POST'])
def main():
    # пришел запрос
    # выдираем из него query json
    request_data = request.get_json()
    data = comparision(request_data)
    # параметры (сформированный json) передаем в функцию (биржу)
    # когда ответ пришел возвращаем json (как написано ниже)
    print("DATA")
    print(data)
    return data
@app.route("/steamSearch", methods=['POST'])
def steam_search():
    request_data = request.get_json()
    data = final_output(request_data["value"])
    return data