import random

import genanki

css = """.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}
"""


def create_fields_list(names):
    fields = [{"name": name} for name in names]
    fields.append({"name": "Audio"})
    return fields


def create_templates(field_names):
    return [
        {
            "name": "Card 1",
            "qfmt": f"{{{{{field_names[1]}}}}}{{{{type:{field_names[0]}}}}}",
            "afmt": (
                f"{{{{FrontSide}}}}"
                f'<hr id="answer">{{{{Audio}}}}{{{{{field_names[0]}}}}}'
            ),
        },
    ]


def generate_anki_id():
    return random.randrange(1 << 30, 1 << 31)


def generate_model(model_name, field_names):
    return genanki.Model(
        generate_anki_id(),
        model_name,
        fields=create_fields_list(field_names),
        templates=create_templates(field_names),
        css=css,
    )


def generate_deck(name):
    return genanki.Deck(generate_anki_id(), name)


def generate_note(model, values):
    values = values.copy()
    last_index = len(values) - 1
    values[last_index] = f"[sound:{values[last_index]}]"
    return genanki.Note(model=model, fields=values)
