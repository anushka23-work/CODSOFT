import json
import os

FILE_NAME = "contacts.json"


def load_contacts():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_contacts(contacts):

    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)