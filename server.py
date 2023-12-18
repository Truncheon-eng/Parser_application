from flask import Flask, request
from comparison_filter import comparision
from find_things import final_output
app = Flask(__name__)


@app.route("/", methods=['POST'])
def main():
    """
    Данная ф-ия вызывается, тогда, когда на сервер приходит POST запрос по ссылке: http://localhost:5000, с целью получения
    данных, отсортированных по определённому значению. Внутри этой ф-ии вызывается другая ф-ия под
    названием comparison_filter, которая и формирует список предметов.
    :return: список отсортированных предметов с разных площадок
    :rtype: list
    """
    request_data = request.get_json()
    info = comparision(request_data)
    return info


@app.route("/steamSearch", methods=['POST'])
def steam_search():
    """
    Данная ф-ия вызывается, тогда, когда на сервер приходит POST запрос по ссылке: http://localhost:5000/steamSearch,
    с целью получения списка предметов какой-то определённой площадки, с помощью которого можно вывести деньги со Steam.
    Внутри этой ф-ии вызывается другая ф-ия под названием final_output, которая и формирует этот список предметов.
    :return: список предметов, состоящий из предемтов, предлагаемых для вывода
    :rtype: list
    """
    request_data = request.get_json()
    data = final_output(request_data["value"])
    return data
