from audiocards.flashcards import create_fields_list


def test_create_fields_list():
    names = ["russisch", "deutsch"]
    expected = [{"name": "russisch"}, {"name": "deutsch"}, {"name": "Audio"}]
    assert create_fields_list(names) == expected
