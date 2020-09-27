import pathlib

from gtts import gTTS

from audiocards.filename import text_to_filename


def text_to_speech(text, language, path, skip_exist=True):
    filename = text_to_filename(text, prefix=f"{language}_", suffix=".mp3")
    filepath = pathlib.Path(path, filename)
    filepath.parent.mkdir(exist_ok=True, parents=True)
    if skip_exist and not filepath.exists():
        tts = gTTS(text, lang=language)
        tts.save(filepath)
        print(f"Saved '{text}' to '{filepath}'")
    else:
        print(f"'{text}' already exists in '{filepath}'")
    return filepath
