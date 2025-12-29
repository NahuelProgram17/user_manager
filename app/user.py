from app.validator import is_valid_email


class User:
    def __init__(self, name: str, email: str):
        if not is_valid_email(email):
            raise ValueError("Email inválido")

        self.name = name
        self.email = email