import pathlib

from audiocards.audio import text_to_speech


def test_text_to_speech():
    filepath = pathlib.Path("test_data/audio/ru_бутерброд.mp3")
    assert not filepath.exists()
    text_to_speech(text="Бутерброд", language="ru", path="test_data/audio/")
    assert filepath.exists()
    text_to_speech(text="Бутерброд", language="ru", path="test_data/audio/")
    filepath.unlink()
