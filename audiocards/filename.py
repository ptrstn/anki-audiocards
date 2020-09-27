import re
import unicodedata


def slugify(text):
    """
    Borrowed from https://docs.djangoproject.com/en/3.0/_modules/django/utils/text/#slugify

    Convert spaces to underscores.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase.
    Strip leading and trailing whitespace.
    """
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "_", text)


def text_to_filename(text, suffix=None, prefix=None):
    filename = text.replace("::", "__")
    filename = slugify(filename)
    if suffix:
        filename = f"{filename}{suffix}"
    if prefix:
        filename = f"{prefix}{filename}"
    return filename
