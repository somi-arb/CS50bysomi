from plates import is_valid

def test_leng():
    assert is_valid("c") == False
    assert is_valid("cs") == True
    assert is_valid("cspython") == False
    assert is_valid("c") == False

def test_first_two_chars():
    assert is_valid("cs") == True
    assert is_valid("00") == False
    assert is_valid("c0") == False
    assert is_valid("") == False

def test_alnum():
    assert is_valid("cs50") == True
    assert is_valid("cs--") == False
    assert is_valid("cat!") == False

def test_i():
    assert is_valid("cs05") == False
    assert is_valid("cs50") == True
    assert is_valid("cs50p") == False
