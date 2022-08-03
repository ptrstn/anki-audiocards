from pathlib import Path

from audiocards.core import create_deck


def test_create_deck():
    csv_path = "csv/russian/vokabeln.csv"
    deck_name = "Test::Russischkurs::VL1"
    language = "ru"

    expected_package_path = Path("test__russischkurs__vl1.apkg")
    assert not expected_package_path.exists()
    create_deck(csv_path=csv_path, language=language, deck_name=deck_name)
    assert expected_package_path.exists()
    expected_package_path.unlink()
