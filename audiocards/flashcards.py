import random

import genanki


def create_fields_list(names):
    return [{"name": name} for name in names]


def create_templates(field_names):
    return [
        {
            "name": "Card 1",
            "qfmt": f"{{{{{field_names[0]}}}}}",
            "afmt": f'{{{{FrontSide}}}}<hr id="answer">{{{{{field_names[1]}}}}}',
        },
        {
            "name": "Card 2",
            "qfmt": f"{{{{{field_names[1]}}}}}",
            "afmt": f'{{{{FrontSide}}}}<hr id="answer">{{{{{field_names[0]}}}}}',
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
    )


def generate_deck(name):
    return genanki.Deck(generate_anki_id(), name)


def generate_note(model, values):
    return genanki.Note(model=model, fields=values)
