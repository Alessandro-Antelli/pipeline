from app.analyzer import analyze_text

def test_analyze_text_basic():
    text = "Ciao mondo 123"
    result = analyze_text(text)
    assert result["words"] == 3
    assert result["numbers"] == 1
    assert result["spaces"] == 2

def test_analyze_text_special_chars():
    text = "hello! @#$"
    result = analyze_text(text)
    assert result["special_chars"] == 4

def test_analyze_text_empty():
    text = ""
    result = analyze_text(text)
    assert result["words"] == 0
    assert result["numbers"] == 0
    assert result["special_chars"] == 0
    assert result["spaces"] == 0