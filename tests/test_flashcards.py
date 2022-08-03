from audiocards.flashcards import create_fields_list, create_back_template


def test_create_fields_list():
    names = ["russisch", "deutsch"]
    expected = [{"name": "russisch"}, {"name": "deutsch"}, {"name": "Audio"}]
    assert create_fields_list(names) == expected


def test_create_back_template():
    expected = """
{{ FrontSide }}<br>
<hr id="answer"><br>
{{ Audio }}<br>
{{ russisch }}
"""
    assert create_back_template("russisch", "deutsch") == expected

