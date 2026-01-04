"""
Unit tests for the KRR package.
Ensures encoding/decoding logic consistency and special character handling.
"""
import krr

def test_round_trip_conversion():
    """
    Verify that encoding followed by decoding restores the original text strictly.
    (Lossless Property Test)
    """
    original_text = "국밥"
    
    # KRR v2.1.1 uses functional approach (krr.encode), not class method
    encoded = krr.encode(original_text)
    decoded = krr.decode(encoded)

    assert original_text == decoded

def test_encode_ignores_non_korean_characters():
    """
    Verify that non-Hangul characters (punctuation, emojis) are preserved as-is,
    and the romanization output follows the v2.1.1 mapping standard.
    """
    test_input = "안녕하세요! 👋"
    
    # Expected output based on v2.2.0 rules:
    # 안(an) + 녕(nyung~) + 하(ha) + 세(sè) + 요(yo)
    # Auto-inserted separator: Backslash (\)
    expected_output = r"an\nyung~\ha\sè\yo\!\ \👋"

    romanized = krr.encode(test_input)

    assert romanized == expected_output
