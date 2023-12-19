import pytest

from comparison_filter import merge
def generate_datas(start_index, finish_index, step):
    data = list()
    for i in range(start_index, finish_index, step):
        data.append({"a": i, "b": 10})
    return data

test_5_res = list()
for i in range(6, 10):
    test_5_res.append({"a": i, "b": 10})
    test_5_res.append({"a": i, "b": 10})

@pytest.mark.parametrize(
    "data_1, data_2, key_, response",
    [
        (generate_datas(5, 10, 1), generate_datas(10, 15, 1), "a", generate_datas(5, 15, 1)),
        (generate_datas(3, 7, 1), generate_datas(7, 10, 1), "a", generate_datas(3, 10, 1)),
        (generate_datas(3, 8, 1), generate_datas(8, 10, 1), "b", generate_datas(3, 10, 1)),
        (generate_datas(3, 9, 2), generate_datas(4, 10, 2), "a", generate_datas(3, 9, 1)),
        (generate_datas(6, 10, 1), generate_datas(6, 10, 1), "a", test_5_res)
    ]
)
def test_merge_function(data_1, data_2, key_, response):
    assert merge(data_1, data_2, key_) == response
