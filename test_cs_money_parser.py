import responses
import json
from config_file import errors
from new_cs_money_parser import find_information

with open('mock/res_http_cs_money.json', 'r', encoding="utf8") as fcc_file:
    http_res_mock = json.load(fcc_file)
with open('mock/data_cs_money_parser.json', 'r', encoding="utf8") as fcc_file:
    assertation_data = json.load(fcc_file)
with open('mock/res_http_cs_money_different.json', 'r', encoding="utf8") as fcc_file:
    different_response = json.load(fcc_file)


@responses.activate
def test_if_res_not_correct_should_return_error():
    responses.get(url="https://cs.money/1.0/market/sell-orders?limit=60&order=asc&sort=price", json={"type": "post"})
    assert find_information({}) == [errors[1]]


@responses.activate
def test_not_200_response_from_server():
    responses.get(url="https://cs.money/1.0/market/sell-orders?limit=60&order=asc&sort=price",
                  json={"error": "No data"}, status=500)
    assert find_information({}) == [errors[2]]


@responses.activate
def test_should_return_correct_answer():
    responses.get(url="https://cs.money/1.0/market/sell-orders?limit=60&order=asc&sort=price", json=http_res_mock)
    assert find_information({}) == assertation_data


@responses.activate
def test_should_add_queryparams_from_arguments():
    responses.get(url="https://cs.money/1.0/market/sell-orders?limit=60&order=asc&sort=price&name=Dragon",
                  json=http_res_mock)
    assert find_information({"name": "Dragon"}) == assertation_data


@responses.activate
def test_should_return_exact_id_from_http_res():
    responses.get(url="https://cs.money/1.0/market/sell-orders?limit=60&order=asc&sort=price", json=http_res_mock)
    assert find_information({}) != different_response
