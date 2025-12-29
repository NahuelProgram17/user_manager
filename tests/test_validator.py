from app.validator import is_valid_email

def test_email_valido():
    assert is_valid_email("test@email.com")

def test_email_invalido():
    assert not is_valid_email("emailinvalido")

def test_email_vacio():
    assert not is_valid_email("")