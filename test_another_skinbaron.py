import responses
from new_skinbaron_parser import find_information
from config_file import errors
import json

sample_dict = {
    "name": "undefined",
    "maxPrice": "undefined",
    "minPrice": "undefined",
    "type": "undefined",
    "quality": "undefined",
    "color": "undefined",
    "hasNameTag": "undefined",
    "hasStickers": "undefined",
    "isSouvenir": "undefined",
    "isStatTrak": "undefined",
    "rarity": "undefined",
    "maxFade": "undefined",
    "minFade": "undefined"
}

with open('mock/data_input_skinbaron.json', 'r', encoding="utf8") as fcc_file:
    returning_data = json.load(fcc_file)
with open('mock/data_skinbaron.json', 'r', encoding="utf8") as fcc_file:
    answer = json.load(fcc_file)
with open('mock/changed_data_skinbaron.json', 'r', encoding="utf8") as fcc_file:
    changed_data = json.load(fcc_file)


@responses.activate
def test_if_aggregatedmetaoffers_is_empty_return_error():
    responses.get(url="https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng",
                  json={"aggregatedMetaOffers": []})
    assert find_information(sample_dict.copy()) == [errors[0]]


@responses.activate
def test_return_correct_answer_if_data_is_valid():
    another_info = sample_dict.copy()
    another_info["type"] = 2
    responses.get(url="https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng&v=2828",
                  json=returning_data)
    assert find_information(another_info) == answer


@responses.activate
def test_status_code_from_server_not_equal_200():
    responses.get(url="https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng",
                  json={"error": "No data"}, status=500)
    assert find_information(sample_dict.copy()) == [errors[2]]


@responses.activate
def test_change_rarity():
    another_info = sample_dict.copy()
    another_info["rarity"] = "Covert"
    responses.get(url="https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng&qf=12",
                  json=changed_data)
    assert find_information(another_info) != answer
