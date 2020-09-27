import genanki
import pandas

from audiocards.audio import text_to_speech
from audiocards.filename import text_to_filename
from audiocards.flashcards import generate_model, generate_deck, generate_note

language = "ru"

df = pandas.read_csv("data/vokabeln.csv", sep="\t")
df.iloc[:, 0].apply(text_to_speech, language=language, path="data/audio")

field_names = list(df)
my_model = generate_model(model_name="ru", field_names=field_names)
my_deck = generate_deck(name="Russisch für Anfänger")

df.loc[:, "audiofile"] = df.iloc[:, 0].apply(
    text_to_filename, prefix=f"{language}_", suffix=".mp3"
)
df.apply(lambda row: my_deck.add_note(generate_note(my_model, row.values)), axis=1)

my_package = genanki.Package(my_deck)
my_package.media_files = [f"data/audio/{file}" for file in list(df.audiofile)]
my_package.write_to_file("russisch.apkg")
