from audiocards.flashcards import create_fields_list


def test_create_fields_list():
    names = ["russisch", "deutsch", "blubb"]
    expected = [{"name": "russisch"}, {"name": "deutsch"}, {"name": "blubb"}]
    assert create_fields_list(names) == expected
