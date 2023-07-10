from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/4') == 25
    assert convert('4/4') == 100
    assert convert('0/4') == 0

def test_gauge():
    assert gauge(25) == '25%'
    assert gauge(100) == 'f'
    assert gauge(0) == 'e'

def test_err():
    with pytest.raises(ValueError):
        convert('three/four')
    with pytest.raises(ZeroDivisionError):
        convert(1/0)
    