import requests
from config_file import errors
from config_file import undefined
maxItems = 5


def find_information(info):
    """
    Ф-ия находит на странице https://cs.money/ maxItems кол-во элементов, соотв. ключам, введёного словаря и
    отфильтровывает параметры этих предметов
    :param info: словарь, содержащий в себе параметры, соотв. query params
    :type info: dict
    :returns: список, содержащий в себе словари, который соотв. каким-то предеметам с сайта https://cs.money/
    :rtype: list
    """
    link = "https://cs.money/1.0/market/sell-orders?limit=60&order=asc&sort=price"
    for element in list(info.keys()):
        if info[element] == undefined:
            del info[element]
    req = requests.get(link, params=info)
    # возвращает мне массив, состоящий из необходимых элементов
    if req.status_code == 200:
        content = req.json()
        # Обработка ошибки
        if content.get("errors") is None:
            # список, в который будет запихнуто огромное кол-во items
            try:
                response_list = []
                items = content.get("items")
                if maxItems > 0:
                    items = items[0:maxItems]
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
                        response["image"] = undefined
                    else:
                        response["image"] = item_asset.get("images").get("steam")
                    keys = ["isSouvenir", "isStatTrak", "rarity", "float"]
                    for keys_element in keys:
                        # цикл для заполнения соответственно таких вещей: response["<>"] = item.asset.get("<>")
                        if item_asset.get(keys_element) is not None:
                            response[keys_element] = item_asset.get(keys_element)
                        else:
                            response[keys_element] = undefined
                    response["stickers"] = []
                    if item["stickers"] is None:
                        response["stickers"] = undefined
                    else:
                        for index_sticker in range(len(item.get("stickers"))):
                            if item.get("stickers")[index_sticker] is not None:
                                response["stickers"].append({"name": item.get("stickers")[index_sticker].get("name")})
                    response["price"] = item.get("pricing").get("computed")
                    response["marketPlace"] = "CS-MONEY"
                    response_list.append(response)
                return response_list
            except Exception:
                return [errors[1]]
        else:
            return [errors[0]]
    else:
        return [errors[2]]
