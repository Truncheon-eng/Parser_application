from new_cs_money_parser import find_information as find_cs_money
from new_skinbaron_parser import find_information as find_skinbaron
# данные, отправляемые на сервер
def merge(data_1, data_2, key_):
    if len(data_1) == 0:
        return data_2
    if len(data_2) == 0:
        return data_1
    if data_1[0][key_] <= data_2[0][key_]:
        return [data_1[0]] + merge(data_1[1:], data_2, key_)
    else:
        return [data_2[0]] + merge(data_2[1:], data_1, key_)
def comparision(dictionary_info):
    # data = list()
    array_filters = ["price", "delivery"]
    sth_filter = array_filters[dictionary_info["params"] - 1]# params = 1 или params = 2
    del dictionary_info["params"]
    data_cs_money = find_cs_money(dictionary_info.copy())
    data_skinbaron = find_skinbaron(dictionary_info.copy())
    print("DATA_CS_MONEY")
    print(data_cs_money)
    print("DATA_SKINBARON")
    print(data_skinbaron)
    # if (data_cs_money[0].get("errors") is not None) and (data_skinbaron[0].get("errors") is None): #TODO: спросить на счёт вот этих проверок
    #     data_skinbaron = data_skinbaron.sort(key=lambda x: x[sth_filter])
    #     data = data_skinbaron
    #     print("No info cs.money")
    # elif (data_skinbaron[0].get("errors") is not None) and (data_cs_money[0].get("errors") is None):
    #     data_cs_money = data_skinbaron.sort(key=lambda x: x[sth_filter])
    #     data = data_cs_money
    #     print("No info cs_baron")
    # elif data_cs_money[0].get("errors") is not None:
    #     data = [data_cs_money[0]]
    # elif data_skinbaron[0].get("errors") is not None:
    #     data = [data_skinbaron[0]]
    if (data_cs_money[0].get("errors") is not None):
        data = data_skinbaron
        print("No info cs.money")
    elif (data_skinbaron[0].get("errors") is not None):
        data = data_cs_money
        print("No info cs_baron")
    else:
        data_cs_money.sort(key=lambda x: x[sth_filter])
        data_skinbaron.sort(key=lambda x: x[sth_filter])
        data = merge(data_cs_money, data_skinbaron, sth_filter)[0:5]
    return data
'''
сортировка будет проходить с помощью filter, но для парметра 1(то есть по цене) это не нужно, 
так как цены уже отсортированы
'''
