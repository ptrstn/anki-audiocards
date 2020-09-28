from audiocards.core import create_deck

csv_path = "data/vokabeln.csv"
language = "ru"
deck_name = "Russisch für Anfänger::LV1"
model_id = 1843843111
deck_id = 1432936755

create_deck(
    csv_path=csv_path,
    language=language,
    deck_name=deck_name,
    deck_id=deck_id,
    model_id=model_id,
)
