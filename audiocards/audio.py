import pathlib

from gtts import gTTS

from audiocards.filename import text_to_filename


def text_to_speech(text, language, path, skip_exist=True):
    """
    :param text: Text to be voiced
    :param language: Language of the text
    :param path: Path to the directory of the mp3 file
    :param skip_exist: Skip if mp3 file already exists
    :return:
    """

    filename = text_to_filename(text, prefix=f"{language}_", suffix=".mp3")
    filepath = pathlib.Path(path, filename)
    filepath.parent.mkdir(exist_ok=True, parents=True)
    if skip_exist and not filepath.exists():
        tts = gTTS(text, lang=language)
        tts.save(filepath)
        print(f'Saved "{text}" to "{filepath}"')
