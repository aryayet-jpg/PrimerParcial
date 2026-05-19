def es_letra(caracter: str) -> bool: 
    return (caracter >= 'A' and caracter <= 'Z') or (caracter >= 'a' and caracter <= 'z')

def es_numero(caracter: str) -> bool:
    return caracter >= '0' and caracter <= '9'

def es_simbolo(caracter: str) -> bool:
    """
     Verifica si un carácter es un símbolo permitido.
    """
    simbolos = '!"#$%&\'()*+,-./'
    for i in range(len(simbolos)):
        if caracter == simbolos[i]:
            return True
    return False


def validar_ingreso(contraseña: str) -> bool:
    """
    Valida que la contraseña cumpla con los requisitos obligatorios de ingreso.
    """
    largo = len(contraseña)
    if largo == 0:
        print("ERROR. La contraseña no puede estar vacia. ")
        return False 
    if largo <8:
        print("INCORRECTA. Debe tener al menos 8 caracteres. ")
        return False
    if contraseña[0] == " ":
        print("Error: No puede comenzar con espacios. ")
        return False

    tiene_letra = False
    for i in range(largo):
        if es_letra(contraseña[i]):
            tiene_letra = True
    
    if not tiene_letra:
        print("Error: Debe contener al menos una letra.")
        return False
    return True

def determinar_nivel(contraseña: str) -> str:
    """
    Analiza la contraseña y determina su nivel de seguridad (Débil, Media o Fuerte).
    """
    largo = len(contraseña)
    tiene_num = False
    tiene_letra = False
    tiene_sim = False

    for i in range(largo):
        if es_letra(contraseña[i]): 
            tiene_letra = True
        if es_numero(contraseña[i]): 
            tiene_num = True
        if es_simbolo(contraseña[i]): 
            tiene_sim = True

        
    if largo >= 12 and tiene_letra and tiene_num and tiene_sim:
        return 'Su contraseña es fuerte.'
    if largo >= 9 and tiene_letra and tiene_num:
        return 'Su contraseña es media.' 
    if largo <= 8 and tiene_letra:
        return 'Su contraseña es debil.'

def contar_tipos(contraseña):
    """
    Cuenta y muestra la cantidad de letras, números, símbolos y espacios.
    """
    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0

    for i in range(len(contraseña)):

        if (contraseña[i] >= 'A' and contraseña[i] <= 'Z') or (contraseña[i] >= 'a' and contraseña[i] <= 'z'):
            letras = letras + 1
            
        if es_numero(contraseña[i]):
            numeros = numeros + 1
            
        if contraseña[i] == " ":
            espacios = espacios + 1
            
        if es_simbolo(contraseña[i]):
            simbolos = simbolos + 1

    print(f"Letras {letras}, Numeros {numeros}, Simbolos {simbolos}, Espacios {espacios}. ")

def buscar_caracter(contraseña):
    """Busca un carácter específico ingresado por el usuario y muestra sus posiciones.
    """

    objetivo = input ("¿Que caracter buscamos?. ")
    contador = 0

    for i in range(len(contraseña)):
        if contraseña[i] == objetivo:
            contador += 1
            print(f"Encontrado en la posición: {i}")

    print(f"Aparece un total de {contador} veces.")

def invertir (contraseña: str) -> str:
    """
    Invierte el orden de los caracteres de la contraseña manualmente.
    """
    invertida = ""
    largo = len(contraseña)

    for i in range(largo):
        posicion_al_reves = largo - 1 - i
        invertida = invertida + contraseña [posicion_al_reves]

    
    return invertida

def es_palindromo(contraseña: str) -> bool:
    """Verifica si la contraseña se lee igual al derecho y al revés.
    """
    invertida = invertir(contraseña)

    if contraseña == invertida:
        return True
    else:
        return False


def ejecucion():
    """
    Función principal que controla el flujo del menú del programa.
    """
    clave_actual = ""
    opcion = ""
    
    while opcion != "8":
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar contraseña.")
        print("2. Validar nivel de seguridad.")
        print("3. Contar tipos de caracteres.")
        print("4. Buscar carácter específico.")
        print("5. Mostrar contraseña invertida.")
        print("6. Generar reporte estadístico.")
        print("7. Verificar si es palíndromo.")
        print("8. Ordenar caracteres de la contraseña.")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ingreso = input("Escriba la contraseña: ")
            if validar_ingreso(ingreso):
                clave_actual = ingreso
                print("¡Clave guardada!")
            
        if opcion == "2":
            print(f"Seguridad: {determinar_nivel(clave_actual)}")
        
        if opcion == "3":
            contar_tipos(clave_actual)
            
        if opcion == "4":
            buscar_caracter(clave_actual)
            
        if opcion == "5":
            print(f"Resultado: {invertir(clave_actual)}")
            
        if opcion == "7":
            if es_palindromo(clave_actual):
                print("¡Es palíndromo!")
            else:
                print("No es palíndromo.")
        if opcion == "9":
            print("Saliendo del programa. Muchas gracias!!")

ejecucion()


















































