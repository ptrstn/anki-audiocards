import argparse

from audiocards import __version__
from audiocards.core import create_deck


def parse_arguments():
    parser = argparse.ArgumentParser(description="An Anki audio flash card generator")

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("csv_path", help="Path to the csv file")
    parser.add_argument("language", help="Language of flash cards")
    parser.add_argument("deck_name", help="Name of the Anki deck")

    return parser.parse_args()


def main():
    args = parse_arguments()
    create_deck(
        csv_path=args.csv_path, language=args.language, deck_name=args.deck_name
    )


if __name__ == "__main__":
    main()
