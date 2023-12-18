from new_cs_money_parser import find_information as find_cs_money
from new_skinbaron_parser import find_information as find_skinbaron


def merge(data_1, data_2, key_):
    """
    Рекурсивная ф-ия принимает на вход два отсортированных списка и делает из них один отсортированный список.
    :param data_1: первый отсортированный список
    :type data_1: list
    :param data_2: второй отсортированный список
    :type data_2: list
    :param key_: ключ, по которому будет происходить сортировка двух списков
    :type key_: str
    :return: возвращает отсортированный список
    :rtype: list
    """
    if len(data_1) == 0:
        return data_2
    if len(data_2) == 0:
        return data_1
    if data_1[0][key_] <= data_2[0][key_]:
        return [data_1[0]] + merge(data_1[1:], data_2, key_)
    else:
        return [data_2[0]] + merge(data_2[1:], data_1, key_)


def comparision(dictionary_info):
    """
    Ф-ия принимает на вход словарь, в зависимости от параметра sth_filter, сортирует предметы,
    получаемые с различных площадок, и выводит их в кол-ве maxItems
    :param dictionary_info: словарь, содержащий в себе параметры, соотв. query params
    :type dictionary_info: dict
    :returns: список, предметов с разных площадок, отсортированных по какому-то фильтру("price", "delivery")
    :rtype: list
    """
    array_filters = ["price", "delivery"]
    sth_filter = array_filters[dictionary_info["params"] - 1]
    del dictionary_info["params"]
    data_cs_money = find_cs_money(dictionary_info.copy())
    data_skinbaron = find_skinbaron(dictionary_info.copy())
    if data_cs_money[0].get("errors") is not None:
        if data_skinbaron[0].get("errors") is None:
            data_skinbaron.sort(key=lambda x: x[sth_filter])
            data = data_skinbaron
        else:
            data = data_skinbaron
    elif data_skinbaron[0].get("errors") is not None:
        if data_cs_money[0].get("errors") is None:
            data_cs_money.sort(key=lambda x: x[sth_filter])
            data = data_cs_money
        else:
            data = data_cs_money
    else:
        data_cs_money.sort(key=lambda x: x[sth_filter])
        data_skinbaron.sort(key=lambda x: x[sth_filter])
        data = merge(data_cs_money, data_skinbaron, sth_filter)[0:5]
    return data
