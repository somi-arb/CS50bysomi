from twttr import shorten


def test_shorten_lower_vowels():
    assert shorten('twitter') == 'twttr'

def test_shorten_upper_vowels():
    assert shorten('twIttEr') == 'twttr'

def test_shorten_lower_n_upper_vowels():
    assert shorten('twitter, fIxIng') == 'twttr, fxng'

def test_shorten_wnum_vowels():
    assert shorten('twitter101') == 'twttr101'

def test_shorten_num():
    assert shorten('101') == '101'

def test_shorten_ponctuation():
    assert shorten('//.._') == '//.._'
