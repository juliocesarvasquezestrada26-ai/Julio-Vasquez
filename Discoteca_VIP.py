# El plan sería este:

'''
1. Preguntar la edad.
2. Preguntar si tiene pase VIP (Sí/No).
3. Si es VIP: Pasa directo.
4. Si no es VIP:
- Si es mayor de 80: Mensaje especial.
- Si es mayor de 18: Pasa normal.
- Si tiene entre 15 y 17: Preguntar si viene con padres.
- De lo contrario: No pasa.
'''

try:
    edad = int(input("Ingrese su edad: "))
    edad_vip = input("¿tiene pase VIP? (si / no): ").lower # .lower se utiliza para convertir a minisculas las letras
    
    if edad_vip == "si":
        print("Bienvenido, pase a la zona privada.")
    elif edad >=18 and edad <=80:
        print("Puede pasar, disfrute la fiesta.") 
    
    # corregir rango de adolescentes
    elif edad >= 15 and edad <18:
        print("Eres menor de edad...")
        acompañado = input("¿vienes con tus padres? (si/no): ").lower
    
        if acompañado == "si":
            print("Acceso concedido. Bienvenidos!" )
        else:
            print("Lo siento, los menores solo entran en compañia de sus padres")
           
    elif edad >80:
        print("¡Respetoss! pase gratis")
    else:
        print("Eres muy joven no puedes pasar.") 
except ValueError:
    print("Error en los datos.")