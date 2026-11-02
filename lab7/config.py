import os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(os.path.join(BASE_DIR, filename))

    if not parser.has_section(section):
        raise Exception(f"Section {section} not found in the {filename} file")

    return dict(parser.items(section))


if __name__ == "__main__":
    print(load_config())
