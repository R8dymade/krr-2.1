"""A test module containting a few test examples to make sure the package still functions as expected."""
from krr_v2 import KRR

def test_encode_decodes_back_to_original():
    """Given a konwn input, ensure the encode decode operation gives the same result."""
    test_word = "국밥"
    romanized = KRR.encode(test_word)

    restored = KRR.decode(romanized)

    assert test_word == restored

def test_encode_ignores_non_korean_characters():
    """Given an input containing special characters, make sure they are just transcribed as is."""
    test_input = "안녕하세요! 👋"

    romanized = KRR.encode(test_input)

    assert romanized == r"e~in\nöng~\he~i\syo\u\!\ \👋"
