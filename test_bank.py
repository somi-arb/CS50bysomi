from bank import value

def test_hello():
    assert value('hello') == '100'
    assert value('hello') == '0'
    assert value('HELLO') == '0'
    assert value('hello') == '0'
    assert value('Hello') == '0'
def test_h():
    assert value('hey') == '20'
    assert value('Hey') == '20'
    assert value('hey') == '20'

def test_other():
    assert value('cat') == '0'
    assert value('cs50') == '100'
    assert value('100') == '100'
    assert value('--< ') == '100'
    assert value('CAT') == '100'
    assert value('cat') == '100'