import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    """Тестируем метод capitalize для корректных входных данных."""
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    """Тестируем метод capitalize для некорректных входных данных."""
    # Проверка работоспособности для стандартных случаев
    assert string_utils.capitalize(input_str) == expected

def test_capitalize_with_none():
    """Проверка, что при передаче None выбрасывается исключение."""
    with pytest.raises(TypeError):
        string_utils.capitalize(None)