# Base de datos ficticia de usuarios y contraseñas
usuarios = {'usuario1': 'contrasena1', 'usuario2': 'contrasena2'}
#store_user = ["german", "tergiversar24"]
def login():
    intentos = 3

    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # Verifica si el usuario existe y la contraseña es correcta
        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario))
            break
        else:
            intentos -= 1
            print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", intentos)

    if intentos == 0:
        print("Número máximo de intentos alcanzado. Cierre de sesión.")

# Ejemplo de uso
login()
