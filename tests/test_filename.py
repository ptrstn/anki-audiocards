from audiocards.filename import text_to_filename


def test_text_to_filename():
    assert text_to_filename(text="hallo", suffix=".mp3") == "hallo.mp3"
    assert text_to_filename("   \tхорошо   ", ".txt") == "хорошо.txt"
    assert text_to_filename("Ландшафт\\\/ ;:;\"", None) == "ландшафт"
    assert text_to_filename("Кто вы? !", None) == "кто_вы"
    assert text_to_filename("Я сошла с ума", prefix="ru_") == "ru_я_сошла_с_ума"
    assert text_to_filename("你好", prefix="zh_", suffix=".mp3") == "zh_你好.mp3"




