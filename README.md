[![Actions Status](https://github.com/ptrstn/anki-audiocards/workflows/Python%20package/badge.svg)](https://github.com/ptrstn/anki-audiocards/actions)
[![Build Status](https://travis-ci.com/ptrstn/anki-audiocards.svg?branch=master)](https://travis-ci.com/ptrstn/anki-audiocards)
[![codecov](https://codecov.io/gh/ptrstn/anki-audiocards/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/anki-audiocards)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# anki-audiocards

An Anki audio flash card generator. 
Takes a tab-delimited CSV file as input and outputs an Anki package.

## Installation

```bash
pip install --user git+https://github.com/ptrstn/anki-audiocards
```

## Usage

```bash
audiocards --help
```

```
usage: audiocards [-h] [--version] [--deck-id DECK_ID] [--model-id MODEL_ID] csv_path language deck_name

An Anki audio flash card generator

positional arguments:
  csv_path             Path to the csv file
  language             Language of flash cards
  deck_name            Name of the Anki deck

optional arguments:
  -h, --help           show this help message and exit
  --version            show program's version number and exit
  --deck-id DECK_ID    Unique deck identifier
  --model-id MODEL_ID  Unique model identifier
```

### Example

```bash
audiocards data/vokabeln.csv ru "Russischkurs::LV1"
```

```
Saved "Добрый вечер" to "data/audio/ru_добрый_вечер.mp3"
Saved "Алла" to "data/audio/ru_алла.mp3"
Saved "привет" to "data/audio/ru_привет.mp3"
[...]
Saved "Ландшафт " to "data/audio/ru_ландшафт.mp3"
Saved "Бутерброд" to "data/audio/ru_бутерброд.mp3"
Generated deck "Russischkurs::VL1" in "russischkurs__lv1.apkg"
```

You can also pass the _deck id_ and _model id_ if you want to update/reuse them in future:

```
audiocards data/vokabeln.csv ru "Russischkurs::LV1" --model-id 1843843111 --deck-id 1432936755
```


## Misc

### List available languages

```bash
gtts-cli --all
```

```
  af: Afrikaans
  ar: Arabic
  bn: Bengali
  bs: Bosnian
  ca: Catalan
  cs: Czech
  cy: Welsh
  da: Danish
  de: German
  el: Greek
  en-au: English (Australia)
  en-ca: English (Canada)
  en-gb: English (UK)
  en-gh: English (Ghana)
  en-ie: English (Ireland)
  en-in: English (India)
  en-ng: English (Nigeria)
  en-nz: English (New Zealand)
  en-ph: English (Philippines)
  en-tz: English (Tanzania)
  en-uk: English (UK)
  en-us: English (US)
  en-za: English (South Africa)
  en: English
  eo: Esperanto
  es-es: Spanish (Spain)
  es-us: Spanish (United States)
  es: Spanish
  et: Estonian
  fi: Finnish
  fr-ca: French (Canada)
  fr-fr: French (France)
  fr: French
  gu: Gujarati
  hi: Hindi
  hr: Croatian
  hu: Hungarian
  hy: Armenian
  id: Indonesian
  is: Icelandic
  it: Italian
  ja: Japanese
  jw: Javanese
  km: Khmer
  kn: Kannada
  ko: Korean
  la: Latin
  lv: Latvian
  mk: Macedonian
  ml: Malayalam
  mr: Marathi
  my: Myanmar (Burmese)
  ne: Nepali
  nl: Dutch
  no: Norwegian
  pl: Polish
  pt-br: Portuguese (Brazil)
  pt-pt: Portuguese (Portugal)
  pt: Portuguese
  ro: Romanian
  ru: Russian
  si: Sinhala
  sk: Slovak
  sq: Albanian
  sr: Serbian
  su: Sundanese
  sv: Swedish
  sw: Swahili
  ta: Tamil
  te: Telugu
  th: Thai
  tl: Filipino
  tr: Turkish
  uk: Ukrainian
  ur: Urdu
  vi: Vietnamese
  zh-CN: Chinese
  zh-cn: Chinese (Mandarin/China)
  zh-tw: Chinese (Mandarin/Taiwan)
```
