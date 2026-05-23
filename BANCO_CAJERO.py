usuario_correcto = "admin"
contraseña_correcta = "admin"
saldo = 10000

def login():
    usuario_correcto = "admin"
    contraseña_correcta = "admin"
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Acceso permitido")
            return True
        intentos -= 1
        if intentos > 0:
            print("Acceso denegado")
            print("Te quedan", intentos, "intentos")
        else:
            print("Acceso denegado")
            print("Has agotado todos los intentos")
            return False

def ver_saldo(saldo):
    print(f"\nSu saldo actual es: {saldo}")

def depositar(saldo):
    try:
        cantidad = float(input("¿Cuanto desea depositar?: "))
        if cantidad <= 0:
            print("Ingrese un numero mayor a cero")
        else:
            saldo += cantidad
            print(f"Su nuevo saldo es: {saldo}")
    except:
        print("Entrada invalida")
    return saldo

def retirar(saldo):
    try:
        cantidad = float(input("¿Cuanto desea retirar?: "))
        if cantidad <= 0:
            print("Cantidad invalida")
        elif cantidad > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= cantidad
            print(f"Su nuevo saldo es: {saldo}")
    except:
        print("Entrada invalida")
    return saldo

def menu(saldo):
    while True:
        print("\n---MENÚ DEL CAJERO---")
        print("1. Ver saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            ver_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "4":
            print("Gracias por usar nuestros servicios.")
            break
        else:
            print("Opción no válida")
    return saldo

# PROGRAMA PRINCIPAL
saldo = 10000
if login():
    saldo = menu(saldo)
