import errno
import os
import re


def strip_text(txt):
    return re.sub("{[^}]*}", "{}", txt)


def get_parts(txt):
    parts = re.findall("{[^}]*}", txt)

    for i, part in enumerate(parts):
        parts[i] = re.sub("[{}]", "", part)

    return tuple(parts)


def read_template(path):
    if not os.path.exists(path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    with open(path, "r") as f:
        lines = f.read()
    return lines


def parse_template(txt):
    return (strip_text(txt), get_parts(txt))


def merge(txt, parts):
    for part in parts:
        txt = txt.replace("{}", f"{part}", 1)

    return txt

if __name__ == "__main__":
    
