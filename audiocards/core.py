import pandas

from audiocards.filename import text_to_filename

df = pandas.read_csv("data/vokabeln_vl1.csv", sep="\t")

language="ru"

df.loc[:, "audio_filename"] = df.iloc[:, 0].apply(text_to_filename, prefix=f"{language}_", suffix=".mp3")
