import re

def is_valid_email(email: str) -> bool:
    """
    Valida si un email tiene un formato correcto.
    Retorna True si es válido, False si no.
    """
    if not email:
        return False

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))
