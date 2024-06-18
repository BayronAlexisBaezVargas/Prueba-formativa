import Funciones
usuarios = {
    "admin": "1234",
    "user": "abcd"
}

usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

if usuario in usuarios and usuarios[usuario] == contrasena:
    print("Autenticación exitosa.\n")
    Funciones.main()
else:
    print("Usuario o contraseña incorrectos. Acceso denegado.\n")
