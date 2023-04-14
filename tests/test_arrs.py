from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], -1, "test") == "Индекс должен быть неотрицательным числом!"
    assert arrs.get([1, 5, 3], -1, "test") != 3
    assert arrs.get([1, 5, 3], -4, "test") == "Индекс должен быть неотрицательным числом!"
    assert arrs.get([1, 3, 5], "1", "test") != 3
    assert arrs.get([1, "3", 5], "1", "test") == "Индекс должен быть целым числом!"
    assert arrs.get(["tester", "3", 5], 1, "test") == "3"
    assert arrs.get("testing", 1, "test") == "Данные должны быть в формате списка!"
    assert arrs.get(1, 1, "test") == "Данные должны быть в формате списка!"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
