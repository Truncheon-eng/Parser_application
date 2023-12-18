import requests
from config_file import errors
from forex_python.converter import CurrencyRates
currency = CurrencyRates()


def output_cs_money(value):
    """
    Ф-ия принимает на вход сумму денег в Steam, и выводит список предметов с сайта https://cs.money/,
    а также их суммарную цену в Steam
    :param value: сумма на кошельке Steam
    :type value: int
    :return: кортеж, состоящий из списка элементов сайта https://cs.money/ и суммы этих элементов в соотв. с площадкой
    Steam
    :rtype: tuple
    """
    link = "https://cs.money/1.0/market/sell-orders?limit=60"
    info = {"minPrice": 0.9*value, "maxPrice": value, "order": "asc", "sort": "price"}
    try:
        req = requests.get(link, params=info)
        response_items = req.json()["items"]
        list_of_items = list()
        sums_of_items = 0
        while (value > 0) and len(response_items) != 0:
            min_diff = response_items[0]["pricing"]["default"] - response_items[0]["pricing"]["computed"]
            index_of_min_elem = 0
            for elem_index in range(len(response_items)):
                diff = (response_items[elem_index]["pricing"]["default"] -
                        response_items[elem_index]["pricing"]["computed"])
                if diff < min_diff:
                    min_diff = diff
                    index_of_min_elem = elem_index
            value -= response_items[index_of_min_elem]["pricing"]["default"]
            if value > 0:
                sums_of_items += response_items[index_of_min_elem]["pricing"]["default"]
                deleted_item = response_items.pop(index_of_min_elem)
                item_pushed = dict()
                item_pushed["name"] = deleted_item.get("asset").get("names").get("short")
                item_pushed["image"] = deleted_item.get("asset").get("images").get("steam")
                item_pushed["info"] = deleted_item.get("seller").get("steamId64")
                list_of_items.append(item_pushed)
        return list_of_items, sums_of_items
    except Exception:
        return errors[1], 0


def output_skinbaron_parser(value):
    """
    Ф-ия принимает на вход сумму денег в Steam, и выводит список предметов с сайта https://skinbaron.de/en,
    а также их суммарную цену в Steam
    :param value: сумма на кошельке Steam
    :type value: int
    :return: кортеж, состоящий из списка элементов сайта https://skinbaron.de/en и суммы этих элементов в соотв. с
    площадкой Steam
    :rtype: tuple
    """
    link = "https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng"
    value = round(currency.get_rates("USD")["EUR"]*value, 2)
    info = {"plb": round(0.9*value, 2), "pub": value}
    try:
        req = requests.get(link, params=info)
        response_items = req.json()["aggregatedMetaOffers"]
        list_of_items = list()
        sums_of_items = 0
        while (value > 0) and len(response_items) != 0:
            min_diff = response_items[0]["steamMarketPrice"] - response_items[0]["singleOffer"]["itemPrice"]
            index_of_min_elem = 0
            for elem_index in range(len(response_items)):
                diff = (response_items[elem_index]["steamMarketPrice"]
                        - response_items[elem_index]["singleOffer"]["itemPrice"])
                if diff < min_diff:
                    min_diff = diff
                    index_of_min_elem = elem_index
            value -= response_items[index_of_min_elem]["steamMarketPrice"]
            if value > 0:
                sums_of_items += response_items[index_of_min_elem]["steamMarketPrice"]
                deleted_item = response_items.pop(index_of_min_elem)
                item_pushed = dict()
                item_pushed["name"] = deleted_item.get("singleOffer").get("localizedName")
                item_pushed["image"] = deleted_item.get("singleOffer").get("imageUrl")
                item_pushed["info"] = "https://skinbaron.de/en/" + deleted_item.get("offerLink")
                list_of_items.append(item_pushed)
        return list_of_items, currency.get_rates("EUR")["USD"]*sums_of_items
    except Exception:
        return errors[1], 0


def final_output(money):
    """
    Ф-ия также принимает на вход кол-во денег на кошельке в Steam, вызывает две предыдущие ф-ии
    и сравнивает значения, которые эти ф-ии возвращают, между собой.
    :param money: это сумма на кошельке в Steam
    :type money: int
    :return: список, состоящий из предметов, предполагаемых для покупки, суммы этих предметов на площадке Steam, а также
    названия площадки, на которой эти предметы можно продать.
    :rtype: list
    """
    cs_money = output_cs_money(money)
    skinbaron = output_skinbaron_parser(money)
    if cs_money[1] > skinbaron[1]:
        response = cs_money[0]
        response.append({"sumsOfItems": cs_money[1]})
        response.append({"marketPlace": "CS-MONEY"})
        return response
    else:
        response = skinbaron[0]
        response.append({"sumsOfItems": skinbaron[1]})
        response.append({"marketPlace": "SKINBARON"})
        return response
