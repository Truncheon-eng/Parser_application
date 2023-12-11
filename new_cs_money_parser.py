import requests
import json
# from forex_python.converter import CurrencyRates # добавление библиотеки, отслеживающий курсы валют
# currency = CurrencyRates()
dictionary_info = {
    "name": "Wasteland Rebel",
    "minPrice": 10.0,
    "maxPrice": 10000000.0,
    "type": 5,
    "quality": "ft",
    "color": "undefind",
    "hasNameTag": "undefind",
    "hasStickers": "true",
    "isSouvenir": "undefind",
    "isStatTrak": "true",
    "rarity": "Covert",
    "minFade": "undefind",
    "maxFade": "undefind",
}
def find_information(info): #info - информация об объекте
    link = "https://cs.money/1.0/market/sell-orders?limit=60"
    #так как я удаляю некоторые параметры, то в info эти парметры уже не содержатся, тогда в info будут содержаться все необходимые для удаления ключи и их значения
    for element in list(info.keys()):
        if info[element] == "undefind":
            del info[element]
    req = requests.get(link, params = info)
    print(req.url)
    content = req.json() #возвращает мне массив, состоящий из необходимых элементов
    if content.get("errors") == None: # Обработка ошибки
        response_list = [] #список, в который будет запихнуто огромное кол-во items
        items = content.get("items")
        if len(items) > 5:
            items = items[0:5]
        for index_item in range(len(items)):
            item, item_asset = items[index_item], items[index_item].get("asset")
            response = {}
            if item.get("seller").get("delivery").get("medianTime") == None:
                response["delivery"] = "undefined"
            else:
                response["delivery"] = item.get("seller").get("delivery").get("medianTime")
            response["name"] = item_asset.get("names").get("short")
            if item_asset.get("images").get("steam") == None:
                response["image"] = "undefind"
            else:
                response["image"] = item_asset.get("images").get("steam")
            # response["isSouvenir"] = item_asset.get("isSouvenir")
            # response["isStatTrak"] = item_asset.get("isStatTrak")
            # response["quality"] = item_asset.get("quality")
            # response["rarity"] = item_asset.get("rarity")
            # response["type"] = item_asset.get("type")
            # response["float"] = item_asset.get("float")
            keys = ["isSouvenir", "isStatTrak", "quality", "rarity", "type", "float"]
            for keys_element in keys:
                response[keys_element] = item_asset.get(keys_element) #цикл для заполнения соответственно таких вещей: response["<>"] = item.asset.get("<>")
            response["stickers"] = []
            if item["stickers"] == None:
                response["stickers"] = "undefind"
            else:
                for index_sticker in range(len(item.get("stickers"))):
                    if item.get("stickers")[index_sticker] != None:
                        response["stickers"].append({"name": item.get("stickers")[index_sticker].get("name")})
            response["price"] = item.get("pricing").get("computed")
            response_list.append(response)
        with open('src/data_cs_money.json', 'w') as file:
            json.dump(response_list, file, indent=4)
        return response_list
    else:
        with open('src/data_cs_money.json', 'w') as file:
            json.dump([{"errors": "Ничего не найдено"}], file, indent=4, ensure_ascii=True)
        return [{"errors": "Ничего не найдено"}]
find_information(dictionary_info)