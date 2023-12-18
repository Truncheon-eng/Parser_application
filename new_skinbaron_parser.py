import requests
from config_file import undefined
from config_file import errors
from config_file import maxItems
# добавление библиотеки, отслеживающий курсы валют
from forex_python.converter import CurrencyRates
currency = CurrencyRates()


def unstandart(info):
    """
    В следствие имутабельности такого типа данных, как словари, данная ф-ия меняет параметры, соответствующие
    стандарту, на параметры, подходящие только под сайт: https://skinbaron.de/en
    :param info: словарь, который соответсвует общему стандарту поиска предметов в приложении
    :type info: dict
    :return: None
    """
    list_of_type = {2: 2828, 7: 2827, 8: 2827, 3: 2826, 4: 2826, 5: 2824, 13: 2908, 6: 2825}
    if info["type"] != undefined:
        info["v"] = list_of_type[info.pop("type")]
    unstandart_list, standart_list = (["str", "sticker", "souvenir", "statTrak"],
                                      ["name", "hasStickers", "isSouvenir", "isStatTrak"])
    for st_list_index in range(len(unstandart_list)):
        if info[standart_list[st_list_index]] != undefined:
            info[unstandart_list[st_list_index]] = info.pop(standart_list[st_list_index])
    if info["minPrice"] != undefined:
        info["plb"] = round(currency.get_rates("USD")["EUR"] * info.pop("minPrice"), 2)
    if info["maxPrice"] != undefined:
        # специальное округление до двух,
        # так как сайт не может обработать значения с большим кол-вом дес. знаков после запятой
        info["pub"] = round(currency.get_rates("USD")["EUR"] * info.pop("maxPrice"), 2)
    if info["quality"] != undefined:
        quality_dict = {"fn": 0, "mw": 1, "ft": 2, "ww": 3, "bs": 4}
        info["quality"] = quality_dict[info["quality"]]
    if info["rarity"] != undefined:
        rarity_list = {"Consumer Grade": 2, "Industrial Grade": 4, "Mil-Spec Grade": 6,
                       "Restricted": 8, "Classified": 10, "Covert": 12}
        info["rarity"] = rarity_list[info["rarity"]]


def find_information(info):
    """
    Ф-ия принимает на вход словарь, передаёт ключи этого словаря в качестве query params, и получает на выходе список
    из maxItems отфильтрованных предметов с сайта https://skinbaron.de/en
    :param info: словарь, содержащий в себе параметры, соотв. query params
    :type info: dict
    :returns: список, содержащий в себе словари, который соотв. каким-то предеметам с сайта https://skinbaron.de/en
    :rtype: list
    """
    unstandart(info)
    for element in list(info.keys()):
        if info[element] == undefined:
            del info[element]
    # CF - позволяет отсортировать список по возрастанию цены
    link = "https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng"
    # проверка статуса присылаемых данных
    if requests.get(link, params=info).status_code == 200:
        response = requests.get(link, params=info).json()
        if len(response.get("aggregatedMetaOffers")) == 0:
            return [errors[0]]
        else:
            try:
                list_of_skins = response.get("aggregatedMetaOffers")
                if maxItems > 0:
                    list_of_skins = list_of_skins[0:maxItems]
                list_of_response = []  # список, состоящий из найденных объектов
                for item_in_list in range(len(list_of_skins)):
                    item_response = {}
                    item = list_of_skins[item_in_list]
                    if item.get("singleOffer").get("tradeLockHoursLeft") is None:
                        item_response["delivery"] = 0
                    else:
                        item_response["delivery"] = (item.get("singleOffer").get("tradeLockHoursLeft"))
                    item_response["name"] = item.get("singleOffer").get("localizedName")
                    item_response["image"] = item.get("singleOffer").get("imageUrl")
                    if item.get("singleOffer").get("souvenirString") is None:
                        item_response["isSouvenir"] = False
                    else:
                        item_response["isSouvenir"] = True
                    if item.get("singleOffer").get("statTrakString") is None:
                        item_response["isStatTrak"] = False
                    else:
                        item_response["isStatTrak"] = True
                    if item.get("singleOffer").get("localizedRarityName") is None:
                        item_response["rarity"] = undefined
                    else:
                        item_response["rarity"] = item.get("singleOffer").get("localizedRarityName")
                    if item.get("singleOffer").get("wearPercent") is None:
                        item_response["float"] = undefined
                    else:
                        item_response["float"] = item.get("singleOffer").get("wearPercent") / 100
                    item_response["stickers"] = []
                    if item.get("singleOffer").get("stickers") is None:
                        item_response["stickers"] = undefined
                    else:
                        for index_sticker in range(len(item.get("singleOffer").get("stickers"))):
                            if item.get("singleOffer").get("stickers")[index_sticker] is not None:
                                item_response["stickers"].append({"name": item.get("singleOffer")
                                                                 .get("stickers")[index_sticker].get("localizedName")})
                    item_response["price"] = round(currency.get_rates("EUR")["USD"]*item.get("singleOffer")
                                                   .get("itemPrice"), 2)
                    item_response["marketPlace"] = "SKINBARON"
                    list_of_response.append(item_response)
                return list_of_response
            except Exception:
                return [errors[1]]
    else:
        return [errors[2]]
