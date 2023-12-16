import requests
# добавление библиотеки, отслеживающий курсы валют
from forex_python.converter import CurrencyRates
currency = CurrencyRates()
maxItems = 5

def replace_values(list_, param_stand, dict_, param_unstand, offset, k):
    for index_elem in range(len(list_)):
        if dict_[param_stand] == list_[index_elem]:
            dict_.pop(param_stand)
            dict_[param_unstand] = index_elem*k + offset
            break
#  функция, которая приводит словарь, который передаётся в качестве параметра, в вид для запроса на исходном сайте


def unstandart(info):
    #TODO: убрать огромное кол-во if-ов
    if info["type"] == 2:
        info.pop("type")
        info["v"] = 2828
    elif info["type"] == 7 or info["type"] == 8:
        info.pop("type")
        info["v"] = 2827
    elif info["type"] == 6:
        info.pop("type")
        info["v"] = 2825
    elif info["type"] == 3 or info["type"] == 4:
        info.pop("type")
        info["v"] = 2826
    elif info["type"] == 5:
        info.pop("type")
        info["v"] = 2824
    elif info["type"] == 13:
        info.pop("type")
        info["v"] = 2908
    unstandart_list, standart_list = (["str", "sticker", "souvenir", "statTrak"],
                                      ["name", "hasStickers", "isSouvenir", "isStatTrak"])
    for st_list_index in range(len(unstandart_list)):
        if info[standart_list[st_list_index]] != "undefined":
            info[unstandart_list[st_list_index]] = info.pop(standart_list[st_list_index])
    if info["minPrice"] != "undefined":
        info["plb"] = round(currency.get_rates("USD")["EUR"] * info.pop("minPrice"), 2)
    if info["maxPrice"] != "undefined":
        # специальное округление до двух,
        # так как сайт не может обработать значения с большим кол-вом дес. знаков после запятой
        info["pub"] = round(currency.get_rates("USD")["EUR"] * info.pop("maxPrice"), 2)
    if info["quality"] != "undefined":
        quality_list = ["fn", "mw", "ft", "ww", "bs"]  # список всевозможных входных качеств
        replace_values(quality_list, "quality", info, "wf", 0, 1)
    if info["rarity"] != "undefined":
        rarity_list = ["Consumer Grade", "Industrial Grade", "Mil-Spec Grade", "Restricted", "Classified", "Covert"]
        replace_values(rarity_list, "rarity", info, "qf", 2, 2)
    # info["maxFade"] = "undefined"
    # info["minFade"] = "undefined"
    # info["color"] = "undefined"
    # info["hasNameTag"] = "undefined"
    info["language"] = "en"


def find_information(info):
    unstandart(info)
    for element in list(info.keys()):
        if info[element] == "undefined":
            del info[element]
    # CF - позволяет отсортировать список по возрастанию цены
    link = "https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng"
    response = requests.get(link, params=info).json() # TODO: сделать проверку на работу сервера requests.get(link, params=info) == 200
    if len(response.get("aggregatedMetaOffers")) == 0:
        return [{"errors": "No information with this request"}] # TODO: вынести undefined, ошибки в отдельную переменную
    else:
        try: # может убрать вместе с catch
            list_of_skins = response.get("aggregatedMetaOffers")
            if maxItems > 0:
                list_of_skins = list_of_skins[0:maxItems]
            list_of_response = []  # список, состоящий из найденных объектов
            for item_in_list in range(len(list_of_skins)):
                item_response = {}
                item = list_of_skins[item_in_list]
                if list_of_skins[item_in_list].get("singleOffer").get("tradeLockHoursLeft") is None:
                    item_response["delivery"] = 0
                else:
                    item_response["delivery"] = list_of_skins[item_in_list].get("singleOffer").get("tradeLockHoursLeft")
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
                item_response["rarity"] = item.get("singleOffer").get("localizedRarityName")
                item_response["float"] = item.get("singleOffer").get("wearPercent") / 100
                item_response["stickers"] = []
                if item.get("singleOffer").get("stickers") is None:
                    item_response["stickers"] = "undefined"
                else:
                    for index_sticker in range(len(item.get("singleOffer").get("stickers"))):
                        item_response["stickers"].append({"name": item.get("singleOffer").get("stickers")[index_sticker].
                                                         get("localizedName")})
                item_response["price"] = round(currency.get_rates("EUR")["USD"]*item.get("singleOffer").get("itemPrice"), 2)
                item_response["marketPlace"] = "SKINBARON"
                list_of_response.append(item_response)
            return list_of_response
        except Exception:
            return [{"errors": "No information about keys"}]
