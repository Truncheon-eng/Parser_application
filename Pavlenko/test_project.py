import pytest
import builtins

def maxFade(value11):
    if value11 == '':
        return 'undefined'
    elif value11.isdigit():
        if int(value11) < 78 or int(value11) > 100:
            tk.messagebox.showinfo('Ошибка ввода', ('Значение градиента должно быть от 78 до 100'))
            return 0
        else:
            return float(value11)
    else:
        tk.messagebox.showinfo('Ошибка ввода', ('Вводите числовые значения градиента'))
        return 0
def test_maxFade_good_input():
    assert maxFade('90') == 90.0
    assert maxFade('79') == 79.0
    assert maxFade('100') == 100.0
    assert maxFade('78') == 78.0
def test_maxFade_empty_string():
    assert maxFade('') == 'undefined'
def test_nonumbers():
    with pytest.raises(Exception):
        value11.isdigit() == False
def test_otrezok():
    with pytest.raises(Exception):
        value11 < 78 or value11 > 100
        maxFade('101')
        maxFade('77')
        maxFade('32')
        
def minPrice(value1):
    allowed_symbols = set("1234567890.")
    if value1 == '':
        return 'undefined'
    for char in value1:
        if char not in allowed_symbols:
            tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода цены должно состоять из числовых значений'))
            return 0
        else:
            return float(value1)
def test_minPrice_empty_string():
    assert minPrice('') == 'undefined'
def test_minPrice_good_input():
    assert minPrice('10.5') == 10.5
    assert minPrice('100') == 100.0
    assert minPrice('0.01') == 0.01
    assert minPrice('123.43543') == 123.43543
def test_minPrice_words_input():
    with pytest.raises(Exception):
        minPrice('abc')
        minPrice('абвгдеё')
def test_minPrice_symbols_input():
    with pytest.raises(Exception):
        minPrice('10,')
        minPrice('()*&^%$#@!')

def sendform(balance):
        if balance != '':
            if balance.isdigit():
                return float(balance)
            else:
                tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода баланса должно состоять из числовых значений'))
                return 0
        else:
            tk.messagebox.showinfo('Ошибка ввода', ('Введите баланс'))
            return 0
def test_sendform_empty_string():
    with pytest.raises(Exception):
        sendform('')
def test_sendform_notnumbers():
    with pytest.raises(Exception):
        balance.isdigit() == False
def test_correct_input():
    assert sendform('100') == 100.0
    assert sendform('20') == 20.0
















    
