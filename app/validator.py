import re

def is_valid_email(email: str) -> bool:
    if not email:
        return False

    email = email.strip()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))
