import requests
maxItems = 5
def find_information(info):
    print("cs_money_parser begin")
    link = "https://cs.money/1.0/market/sell-orders?limit=60"
    # так как я удаляю некоторые параметры, то в info эти парметры уже не содержатся,
    # тогда в info будут содержаться все необходимые для удаления ключи и их значения
    ### TODO: "order": "asc"
    for element in list(info.keys()):
        if info[element] == "undefined":
            del info[element]
    info["order"] = "asc"
    req = requests.get(link, params=info) # TODO: посмотреть на код, который мне пришёл
    print(req.url) #TODO: УБРАТЬ ЕГО
    # возвращает мне массив, состоящий из необходимых элементов
    content = req.json()
    # Обработка ошибки
    if content.get("errors") is None:
        # список, в который будет запихнуто огромное кол-во items
        try:
            response_list = []
            items = content.get("items")
            if maxItems > 0:
                items = items[0:maxItems]
            # if len(items) > 5:
            #     items = items[0:5]
            for index_item in range(len(items)):
                item, item_asset = items[index_item], items[index_item].get("asset")
                response = {}
                if item.get("seller").get("delivery").get("medianTime") is None:
                    # так как отсутствие говорит, о том что скин можно доставить мгновенно
                    response["delivery"] = 0
                else:
                    response["delivery"] = item.get("seller").get("delivery").get("medianTime")
                response["name"] = item_asset.get("names").get("short")
                if item_asset.get("images").get("steam") is None:
                    response["image"] = "undefined" #TODO: заменить все повт. undefined на переменную
                else:
                    response["image"] = item_asset.get("images").get("steam")
                keys = ["isSouvenir", "isStatTrak", "rarity", "float"] #TODO: отвести всё в переменную общую
                for keys_element in keys:
                    # цикл для заполнения соответственно таких вещей: response["<>"] = item.asset.get("<>")
                    response[keys_element] = item_asset.get(keys_element)
                response["stickers"] = []
                if item["stickers"] is None:
                    response["stickers"] = "undefined"
                else:
                    for index_sticker in range(len(item.get("stickers"))):
                        if item.get("stickers")[index_sticker] is not None:
                            response["stickers"].append({"name": item.get("stickers")[index_sticker].get("name")})
                response["price"] = item.get("pricing").get("computed")
                response["marketPlace"] = "CS-MONEY"
                response_list.append(response)
                return response_list
        except Exception:
            return [{"errors": "No information about keys"}] #TODO: заменить список на объект item или errors
    else:
        return [{"errors": "No information with this request"}]