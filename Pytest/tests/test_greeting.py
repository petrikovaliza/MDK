from my_src.greeting import Text_Greeting
import pytest

@pytest.mark.greeting
@pytest.mark.parametrize('test_input, expected', [("Liza", "My name Liza"), ("Oleg", "My name Oleg")])
def test_greeting(test_input, expected):
    assert Text_Greeting().greeting(test_input) == expected
    
@pytest.mark.greeting
def test_empty():
    assert Text_Greeting().empty_string(True)

@pytest.mark.greeting
def test_register():
    assert Text_Greeting().register_check(input) == 'up'.upper()

@pytest.mark.greeting
def test_long():
    assert Text_Greeting().long_check(True)

@pytest.mark.greeting
def test_type():
    assert Text_Greeting().string_type(True)
