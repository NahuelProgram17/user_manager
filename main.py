from app.user import User
from app.storage import save_user


def main():
    name = input("Nombre: ")
    email = input("Email: ")

    try:
        user = User(name, email)
        save_user(user)
        print("Usuario guardado correctamente ✅")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()