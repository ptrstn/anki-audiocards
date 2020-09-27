import pandas

from audiocards.audio import text_to_speech

df = pandas.read_csv("data/vokabeln.csv", sep="\t")

language = "ru"

df.iloc[:, 0].apply(text_to_speech, language="ru", path="data/audio")
