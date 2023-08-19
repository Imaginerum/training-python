def autentykator(a,b):
    credential = {
        "Halina":"12345678",
        "Gabrysia":"coruscurus",
        "Piotr":"kopacz"

    }
    if credential[a] == b:
        print("zgadza sie")
        return True

    else:
        print("nie zgadza sie")
        return False


UserName = input("POdaj nazwę użytkownika: ")
password = input("Podaj hasło użytkownika: ")
autentykator(UserName, password)