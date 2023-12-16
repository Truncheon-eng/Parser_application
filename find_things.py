import requests
from forex_python.converter import CurrencyRates
currency = CurrencyRates()

def output_cs_money(value):
    link = "https://cs.money/1.0/market/sell-orders?limit=60"
    '''
    первая причина, по которой я предаю в качестве минимальной цены значение равное 0,9
    это очень большая нагрузка на сервер в таком случае,  + в среденем, почему-то цена для предметов в диапозоне больших чисел, 
    т.е. то в примере от 4500 до 5000 цена скинов в стиме будет больше, чем в том же самом опыте с 0 до 5000.
    '''
    info = {"minPrice": 0.9*value, "maxPrice": value, "order": "asc"} #asc - значение ключа, выстраивающего все предмета от минимальной до макс. цены
    '''
    try и except специально добавлены, так как может произойти такое, что сервак вернёт json, в котором просто 
    отсутсвуют необходимые нам элементы
    '''
    try:
        req = requests.get(link, params=info)
        response_items = req.json()["items"]
        list_of_items = list()
        sums_of_items = 0
        while (value > 0) and len(response_items) != 0:
            min_diff = response_items[0]["pricing"]["default"] - response_items[0]["pricing"]["computed"]
            index_of_min_elem = 0
            for elem_index in range(len(response_items)):
                diff = response_items[elem_index]["pricing"]["default"] - response_items[elem_index]["pricing"]["computed"]
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
                item_pushed["info"] =deleted_item.get("seller").get("steamId64")
                list_of_items.append(item_pushed)
        return list_of_items, sums_of_items
    except KeyError:
        return [{"errors": "There's nothing here"}, 0]
def output_skinbaron_parser(value):
    link = "https://skinbaron.de/api/v2/Browsing/FilterOffers?appId=730&sort=CF&language=eng"
    info = {"plb": round(currency.get_rates("USD")["EUR"] * value * 0.9, 2), "pub": round(currency.get_rates("USD")["EUR"] * value, 2)}
    try:
        req = requests.get(link, params=info)
        response_items = req.json()["aggregatedMetaOffers"]
        list_of_items = list()
        sums_of_items = 0
        while (value > 0) and len(response_items) != 0:
            min_diff = response_items[0]["steamMarketPrice"] - response_items[0]["singleOffer"]["itemPrice"]
            index_of_min_elem = 0
            for elem_index in range(len(response_items)):
                diff = response_items[elem_index]["steamMarketPrice"] - response_items[elem_index]["singleOffer"]["itemPrice"]
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
    except KeyError:
        return [{"errors": "There's nothing here"}, 0]
def final_output(money):
    cs_money = output_cs_money(money)
    skinbaron = output_skinbaron_parser(money)
    if cs_money[1] > skinbaron[1]:
        response = cs_money[0]
        response.append({"sumsOfItems": round(cs_money[1], 2)})
        response.append({"marketPlace": "CS-MONEY"})
        return response
    else:
        response = skinbaron[0]
        response.append({"sumsOfItems": round(skinbaron[1], 2)})
        response.append({"marketPlace": "SKINBARON"})
        return response

