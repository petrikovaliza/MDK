from my_src.calc import Calculation
import pytest

@pytest.mark.calc
def test_sum():
    assert Calculation().sum(4, 7) == 11
    
@pytest.mark.calc
def test_sub():
    assert Calculation().sub(7, 2) == 5
    
@pytest.mark.calc
def test_multiply():
    assert Calculation().multiply(2, 2) == 4
    
@pytest.mark.calc
def test_div():
    assert Calculation().div(40, 5) == 8
    
@pytest.mark.skip("Мусор")
def test_invisible():
    assert 33 == 5

@pytest.mark.calc
def test_find_palyndrome():
    assert Calculation().find_palyndrome(True)