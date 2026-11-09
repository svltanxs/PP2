import os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        # Fallback if filename was misspelled as datebase.ini
        alt_path = os.path.join(BASE_DIR, "datebase.ini")
        if os.path.exists(alt_path):
            path = alt_path

    parser.read(path)

    if not parser.has_section(section):
        raise Exception(f"Section {section} not found in the {filename} file")

    return dict(parser.items(section))


if __name__ == "__main__":
    print(load_config())
