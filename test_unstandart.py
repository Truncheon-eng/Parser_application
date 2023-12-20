# from unittest.mock import Mock
from config_file import undefined
from new_skinbaron_parser import unstandart
from mock.arguments_for_parser import sample_dict
# import forex_python.converter

# ВСЁ ЧТО ЗАКОММЕНЧЕНО ИСПОЛЬЗУЕТСЯ В СЛУЧАЕ, ЕСЛИ FOREX_PYTHON ПОДКЛЮЧЕН


def test_change_undefind_values():
    # forex_python.converter.CurrencyRates.get_rates = Mock()
    # forex_python.converter.CurrencyRates.get_rates.return_value = {"EUR": 2}
    filters = sample_dict.copy()
    assert filters.get("hasNameTag") == undefined
    unstandart(filters)
    assert filters.get("hasNameTag") != undefined


def test_change_key_of_name():
    # forex_python.converter.CurrencyRates.get_rates = Mock()
    # forex_python.converter.CurrencyRates.get_rates.return_value = {"EUR": 2}
    filters = sample_dict.copy()
    unstandart(filters)
    assert filters.get("str") == "Dragon Lore"


def test_change_price_value():
    # forex_python.converter.CurrencyRates.get_rates = Mock()
    # forex_python.converter.CurrencyRates.get_rates.return_value = {"EUR": 2}
    filters = sample_dict.copy()
    unstandart(filters)
    # assert filters["plb"] == 140.00
    # assert filters["pub"] == 200.00
    assert filters["plb"] == 63.0
    assert filters["pub"] == 90.0


def test_of_changing_type_and_quality():
    # forex_python.converter.CurrencyRates.get_rates = Mock()
    # forex_python.converter.CurrencyRates.get_rates.return_value = {"EUR": 2}
    filters = sample_dict.copy()
    filters["type"] = 2
    unstandart(filters)
    assert filters["v"] == 2828
    assert filters["wf"] == 0


def test_of_undefined_value_type():
    # forex_python.converter.CurrencyRates.get_rates = Mock()
    # forex_python.converter.CurrencyRates.get_rates.return_value = {"EUR": 2}
    filters = sample_dict.copy()
    filters["type"] = undefined
    unstandart(filters)
    assert filters.get("v") is None
    assert filters.get("type") is None


def test_minfade_maxfade():
    # forex_python.converter.CurrencyRates.get_rates = Mock()
    # forex_python.converter.CurrencyRates.get_rates.return_value = {"EUR": 2}
    filters = sample_dict.copy()
    assert filters["minFade"] == 80
    assert filters["maxFade"] == 100
    unstandart(filters)
    assert filters.get("minFade") is None
    assert filters.get("maxFade") is None
