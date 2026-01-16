import json
import os

FILE_PATH = "users.json"


def load_users():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_user(user):
    users = load_users()

    users.append({
        "name": user.name,
        "email": user.email
    })

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)