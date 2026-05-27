#!/usr/bin/env python3
"""Module serialisation"""

import json


def serialize_and_save_to_file(data, filename):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
