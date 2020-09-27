import genanki
import pandas

from audiocards.audio import text_to_speech
from audiocards.flashcards import generate_model, generate_deck, generate_note

df = pandas.read_csv("data/vokabeln.csv", sep="\t")

language = "ru"

df.iloc[:, 0].apply(text_to_speech, language="ru", path="data/audio")

field_names = list(df)
my_model = generate_model(model_name="ru", field_names=field_names)
my_deck = generate_deck(name="Russisch für Anfänger")

df.apply(lambda row: my_deck.add_note(generate_note(my_model, row.values)), axis=1)

package = genanki.Package(my_deck)
package.write_to_file("russisch.apkg")
