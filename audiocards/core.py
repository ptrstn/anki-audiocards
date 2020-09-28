import genanki
import pandas

from audiocards.audio import text_to_speech
from audiocards.filename import text_to_filename
from audiocards.flashcards import generate_model, generate_deck, generate_note


def create_deck(csv_path, language, deck_name):
    language = language

    df = pandas.read_csv(csv_path, sep="\t")
    df.iloc[:, 0].apply(text_to_speech, language=language, path="data/audio")

    field_names = list(df)
    my_model = generate_model(model_name=language, field_names=field_names)
    my_deck = generate_deck(name=deck_name)

    df.loc[:, "audiofile"] = df.iloc[:, 0].apply(
        text_to_filename, prefix=f"{language}_", suffix=".mp3"
    )
    df.apply(lambda row: my_deck.add_note(generate_note(my_model, row.values)), axis=1)

    my_package = genanki.Package(my_deck)
    my_package.media_files = [f"data/audio/{file}" for file in list(df.audiofile)]
    package_path = f"{text_to_filename(deck_name)}.apkg"
    my_package.write_to_file(package_path)
    print(f'Generated deck "{deck_name}" in "{package_path}"')
