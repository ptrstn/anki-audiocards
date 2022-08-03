import random

import genanki

css = """
.card {
 font-family: Helvetica;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: ghostwhite;
}

.front {
 background-color: midnightblue;	
 color: white;
 margin: 0;
 font-size: 45px;
 line-height: 150px;
}

.question {
 background-color: black;	
 color: white;
 margin: 0;
 font-size: 23px;
 line-height: 46px;
 margin-bottom: 10px;
}

input{
 text-align: center;
 height: 50px;
 margin: 10px;
 border: 0:
 outline-style: none;
}
"""

front_template_fstring = """
<div class="front">{{{{{language_from}}}}}</div>
<div class="question">{language_from} -> {language_to}</div>
<div class="input">{{{{type:{language_to}}}}}</div>
"""

back_template_fstring = """
{{{{ FrontSide }}}}<br>
<hr id="answer"><br>
{{{{ Audio }}}}<br>
{{{{ {language_to} }}}}
"""


def create_front_template(*fields):
    return front_template_fstring.format(language_from=fields[1], language_to=fields[0])


def create_back_template(*fields):
    return back_template_fstring.format(language_to=fields[0])


def create_fields_list(names):
    fields = [{"name": name} for name in names]
    fields.append({"name": "Audio"})
    return fields


def create_templates(field_names):
    return [
        {
            "name": "Card 1",
            "qfmt": (
                f"{{{{{field_names[1]}}}}}<br>\n"
                f"{{{{type:{field_names[0]}}}}}\n"
            ),
            "afmt": (
                f"{{{{FrontSide}}}}<br>\n"
                f'<hr id="answer"><br>\n'
                f"{{{{Audio}}}}<br>\n"
                f"{{{{{field_names[0]}}}}}\n"
            ),
        },
    ]


def generate_anki_id():
    return random.randrange(1 << 30, 1 << 31)


def generate_model(model_name, field_names, identifier=None):
    return genanki.Model(
        identifier if identifier else generate_anki_id(),
        model_name,
        fields=create_fields_list(field_names),
        templates=create_templates(field_names),
        css=css,
    )


def generate_deck(name, identifier=None):
    return genanki.Deck(identifier if identifier else generate_anki_id(), name)


def generate_note(model, values):
    values = values.copy()
    last_index = len(values) - 1
    values[last_index] = f"[sound:{values[last_index]}]"
    return genanki.Note(model=model, fields=values)
