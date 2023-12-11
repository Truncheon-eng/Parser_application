import requests
import json
from forex_python.converter import CurrencyRates # добавление библиотеки, отслеживающий курсы валют
currency = CurrencyRates()
def replace_values(list_, param_stand, dict_, param_unstand, offset, k):
    for index_elem in range(len(list_)):
        if dict_[param_stand] == list_[index_elem]:
            dict_.pop(param_stand)
            dict_[param_unstand] = index_elem*k + offset
            break
def unstandart(info): #функция, которая приводит словарь, который передаётся в качестве параметра, в вид для запроса на исходном сайте
    if (info["type"] == 2):
        info.pop("type")
        info["v"] = 2828
    elif (info["type"] == 7 or info["type"] == 8):
        info.pop("type")
        info["v"] = 2827
    elif (info["type"] == 6):
        info.pop("type")
        info["v"] = 2825
    elif (info["type"] == 3 or info["type"] == 4):
        info.pop("type")
        info["v"] = 2826
    elif (info["type"] == 5):
        info.pop("type")
        info["v"] = 2824
    elif (info["type"] == 13):
        info.pop("type")
        info["v"] = 2908
    unstandart_list, standart_list = ["str", "sticker", "souvenir", "statTrak"], ["name", "hasStickers", "isSouvenir", "isStatTrak"]
    for st_list_index in range(3):
        if info[standart_list[st_list_index]] != "undefind":
            info[unstandart_list[st_list_index]] = info.pop(standart_list[st_list_index])
    if info["minPrice"] != "undefind":
        info["plb"] = round(currency.get_rates("USD")["EUR"] * info.pop("minPrice"), 2)
    if info["maxPrice"] != "undefind":
        info["pub"] = round(currency.get_rates("USD")["EUR"] * info.pop("maxPrice"), 2) #специальное округление до двух, так как сайт не может обработать значения с большим кол-вом дес. знаков после запятой
    if info["quality"] != "undefind":
        quality_list = ["fn", "mw", "ft", "ww", "bs"]  # список всевозможных входных качеств
        replace_values(quality_list, "quality", info, "wf", 0, 1)
    if info["rarity"] != "undefind":
        rarity_list = ["Consumer Grade", "Industrial Grade", "Mil-Spec Grade", "Restricted", "Classified", "Covert"]
        replace_values(rarity_list, "rarity", info, "qf", 2, 2)
    info["maxFade"] = "undefind"
    info["minFade"] = "undefind"
    info["color"] = "undefind"
    info["hasNameTag"] = "undefind"
    info["language"] = "en"
def find_information(info):
    unstandart(info)
    for element in list(info.keys()):
        if info[element] == "undefind":
            del info[element]
    link = "https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=PA&language=eng"
    response = requests.get(link, params=info).json()
    if response.get("aggregatedMetaOffers") == []:
        with open('src/data_skinbaron.json', 'w') as file:
            json.dump([{"errors": "No information with this request"}], file, indent=4)
        return [{"errors": "No information with this request"}]
    else:
        list_of_skins = response.get("aggregatedMetaOffers")
        if len(list_of_skins) > 5:
            list_of_skins = list_of_skins[0:5]
        list_of_response = []  # список, состоящий из найденных объектов
        for item_in_list in range(len(list_of_skins)):
            item_response = {}
            item = list_of_skins[item_in_list]
            if list_of_skins[item_in_list].get("singleOffer").get("tradeLockHoursLeft") == None:
                item_response["delivery"] = 0
            else:
                item_response["delivery"] = list_of_skins[item_in_list].get("singleOffer").get("tradeLockHoursLeft")
            item_response["name"] = item.get("singleOffer").get("localizedName")
            item_response["image"] = item.get("singleOffer").get("imageUrl")
            if item.get("singleOffer").get("souvenirString") == None:
                item_response["isSouvenir"] = False
            else:
                item_response["isSouvenir"] = True
            if item.get("singleOffer").get("statTrakString") == None:
                item_response["isStatTrak"] = False
            else:
                item_response["isStatTrak"] = True
            item_response["quality"] = item.get("singleOffer").get("exteriorClassName")
            item_response["rarity"] = item.get("singleOffer").get("localizedRarityName")
            item_response["float"] = item.get("singleOffer").get("wearPercent") / 100
            item_response["stickers"] = []
            if item.get("singleOffer").get("stickers") == None:
                item_response["stickers"] = "undefind"
            else:
                for index_sticker in range(len(item.get("singleOffer").get("stickers"))):
                    item_response["stickers"].append({"name": item.get("singleOffer").get("stickers")[index_sticker].get("localizedName")})
            item_response["price"] = round(currency.get_rates("EUR")["USD"]*item.get("singleOffer").get("itemPrice"), 2)
            list_of_response.append(item_response)
        with open('src/data_skinbaron.json', 'w') as file:
            json.dump(list_of_response, file, indent=4, ensure_ascii=True)
        return list_of_response
