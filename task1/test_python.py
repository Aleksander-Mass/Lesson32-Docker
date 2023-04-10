import math
"""
1. В проекте создать новый модуль test_python.py
2. В модуле написать тесты для встроенных функций
filter, map, sorted, а также для функций из библиотеки
math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
"""


def test_filter():
    numbers = [-2,-3,-1,0,-1,1,3,2]
    positive_numbers = filter(lambda a: a > 0, numbers)
    assert list(positive_numbers) == [1, 3, 2]

    text = 'q12w34rty'
    assert list(filter(set, text)) == ['q', '1', '2', 'w', '3', '4', 'r', 't', 'y']

def test_map():
    numbers = [-2, -1, 0, 1, 2]
    text = ['q', '1', '2', 'w']
    bools = [True, False, False]

    assert list(map(lambda a: a*2, numbers)) == [-4, -2, 0, 2, 4]
    assert  list(map(lambda a: a*2, text)) == ['qq', '11', '22', 'ww']
    assert list(map(lambda a: a*2,bools)) == [2, 0, 0]

def test_sorted():
    numbers = [-4,-3,2,3,0,-1,4]
    text = 'q12w34rty'
    _dict = {'B':3, 'A':4, 'D':5, 'C': 2}

    assert sorted(numbers) == [-4,-3,-1,0,2,3,4]
    assert sorted(text) == ['1', '2', '3', '4', 'q', 'r', 't', 'w', 'y']
    assert sorted(_dict) == ['A', 'B', 'C', 'D']

def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt():
    sqrt_dict = {25:5, 16:4, 4:2}

    for k, v in sqrt_dict.items():
        assert math.sqrt(k) == v

    for num in range(100):
        assert math.sqrt(num*num) == num

def test_pow():
    for num in range(100):
        assert math.pow(num, 2) == num**2

def test_hypot():
    for num in range(100):
        assert math.hypot(num, 2) == math.sqrt(num*num + 2*2)
        assert math.hypot(4, num) == (4*4 + num*num)**0.5