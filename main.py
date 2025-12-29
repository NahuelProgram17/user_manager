from app.user import User

def main():
    print("=== Registro de Usuarios ===")

    name = input("Nombre: ")
    email = input("Email: ")

    try:
        user = User(name, email)
        print("\nUsuario creado correctamente")
        print(f"Nombre: {user.name}")
        print(f"Email: {user.email}")
    except ValueError as error:
        print("\nError:", error)

if __name__ == "__main__":
    main()