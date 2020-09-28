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
usage: audiocards [-h] [--version] csv_path language deck_name

An Anki audio flash card generator

positional arguments:
  csv_path    Path to the csv file
  language    Language of flash cards
  deck_name   Name of the Anki deck

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

### Example

```bash
audiocards data/vokabeln.csv ru "Russischkurs::VL1"
```

```
Saved "Добрый вечер" to "data/audio/ru_добрый_вечер.mp3"
Saved "Алла" to "data/audio/ru_алла.mp3"
Saved "привет" to "data/audio/ru_привет.mp3"
[...]
Saved "Ландшафт " to "data/audio/ru_ландшафт.mp3"
Saved "Бутерброд" to "data/audio/ru_бутерброд.mp3"
Generated deck "Russischkurs::VL1" in "russischkurs__vl1.apkg"
```
