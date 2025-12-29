import json
from app.user import User

FILE_PATH = "users.json"

def save_user(user: User):
    data = {
        "name": user.name,
        "email": user.email
    }

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(data)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)