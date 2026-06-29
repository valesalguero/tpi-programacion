
# ─────────────────────────────────────────────
#  INGRESO DE USUARIO
# ─────────────────────────────────────────────

print("========================================")
print("          Play.in EduGames       ")
print("========================================")
usuario = input("  Ingresa tu nombre de usuario: ")
print(f"\n  Bienvenido, {usuario}!")

# ─────────────────────────────────────────────
#  JUEGO 1 - Adivina el numero
# ─────────────────────────────────────────────

def adivina_numero():
    print("========================================")
    print("   ADIVINA EL NUMERO  (1 - 100)")
    print("========================================")

    semilla = int(input("Ingresa cualquier numero para empezar: "))
    secreto = (semilla % 100) + 1
    intentos = 0

    print("\nTenes 8 intentos. Buena suerte!\n")

    while intentos < 8:
        entrada = input(f"  Intento {intentos + 1}/8 -> ")
        try:
            guess = int(entrada)
        except:
            print("  Ingresa un numero entero.")
        else:
            intentos += 1
            if guess < secreto:
                print("  Demasiado bajo.\n")
            elif guess > secreto:
                print("  Demasiado alto.\n")
            else:
                print(f"\n  Correcto! Lo adivinaste en {intentos} intento(s).")
                return f"gano en {intentos} intentos"

    print(f"\n  Te quedaste sin intentos. El numero era {secreto}.")
    return "perdio"

# ─────────────────────────────────────────────
#  JUEGO 2 - Piedra, Papel, Tijeras
# ─────────────────────────────────────────────

def piedra_papel_tijeras():
    print("========================================")
    print("   PIEDRA, PAPEL O TIJERAS")
    print("========================================")

    gana_contra = {"piedra": "tijeras", "papel": "piedra", "tijeras": "papel"}
    opciones = ["piedra", "papel", "tijeras"]

    puntos_j = 0
    puntos_pc = 0
    contador = 0

    print("Jugamos 5 rondas.\n")

    for ronda in range(1, 6):
        print(f"  -- Ronda {ronda} --")
        eleccion = input("  Tu eleccion (piedra / papel / tijeras): ")
        contador += ronda

        if eleccion not in opciones:
            print("  Opcion invalida, se cuenta como ronda perdida.\n")
            puntos_pc += 1
        else:
            pc = opciones[contador % 3]
            print(f"  PC eligio: {pc}")
            if eleccion == pc:
                print("  Empate\n")
            elif gana_contra[eleccion] == pc:
                print("  Ganaste esta ronda!\n")
                puntos_j += 1
            else:
                print("  Perdiste esta ronda.\n")
                puntos_pc += 1

    print(f"  Resultado -> Vos: {puntos_j}  |  PC: {puntos_pc}")
    if puntos_j > puntos_pc:
        print("  Ganaste el partido!")
        return f"gano {puntos_j}-{puntos_pc}"
    elif puntos_j < puntos_pc:
        print("  Perdiste el partido.")
        return f"perdio {puntos_j}-{puntos_pc}"
    else:
        print("  Empate total!")
        return f"empate {puntos_j}-{puntos_pc}"

# ─────────────────────────────────────────────
#  JUEGO 3 - Mayor o Menor
# ─────────────────────────────────────────────

def mayor_o_menor():
    print("========================================")
    print("   MAYOR O MENOR")
    print("========================================")
    print("Aparece una carta. Decidi si la siguiente")
    print("sera mayor (M) o menor (N). 7 rondas.\n")

    semilla = int(input("Ingresa cualquier numero para empezar: "))
    carta_actual = (semilla % 12) + 1
    aciertos = 0

    for ronda in range(1, 8):
        print(f"\n  Ronda {ronda}/7")
        print(f"  Carta actual: {carta_actual}")
        respuesta = input("  La siguiente sera mayor (M) o menor (N)? ")

        if respuesta != "M" and respuesta != "N" and respuesta != "m" and respuesta != "n":
            print("  Respuesta invalida, se cuenta como error.")
            carta_actual = (semilla + ronda * 3) % 12 + 1
        else:
            carta_siguiente = (semilla + ronda * 13 + aciertos * 5) % 12 + 1
            print(f"  Carta siguiente: {carta_siguiente}")

            if carta_siguiente == carta_actual:
                print("  Empate, no suma ni resta.")
            elif (respuesta == "M" or respuesta == "m") and carta_siguiente > carta_actual:
                print("  Correcto!")
                aciertos += 1
            elif (respuesta == "N" or respuesta == "n") and carta_siguiente < carta_actual:
                print("  Correcto!")
                aciertos += 1
            else:
                print("  Incorrecto!")

            carta_actual = carta_siguiente

    print(f"\n  Aciertos: {aciertos} / 7")
    if aciertos >= 6:
        print("  Excelente!")
    elif aciertos >= 4:
        print("  Bien!")
    else:
        print("  Mala suerte, segui intentando.")
    return f"{aciertos}/7 aciertos"

# ─────────────────────────────────────────────
#  JUEGO 4 - Trivia
# ─────────────────────────────────────────────

PREGUNTAS = [
    ("Cuanto es 12 x 12?",                               "144"),
    ("En que continente esta Brasil?",                   "america"),
    ("Cuantos lados tiene un hexagono?",                 "6"),
    ("Cual es el planeta mas grande del sistema solar?", "jupiter"),
    ("Cuantos meses tiene un anio?",                     "12"),
    ("Cuanto es la raiz cuadrada de 81?",                "9"),
    ("Cual es el animal mas rapido del mundo?",          "guepardo"),
    ("Cuantos jugadores tiene un equipo de futbol?",     "11"),
    ("En que pais esta la Torre Eiffel?",                "francia"),
    ("Cuanto es 7 x 8?",                                "56"),
]

def trivia():
    print("========================================")
    print("         TRIVIA")
    print("========================================")
    print("10 preguntas. Escribi tu respuesta.\n")

    correctas = 0

    for num in range(10):
        pregunta, respuesta = PREGUNTAS[num]
        print(f"  Pregunta {num + 1}: {pregunta}")
        entrada = input("  Tu respuesta: ")

        if entrada == respuesta:
            print("  Correcto!\n")
            correctas += 1
        else:
            print(f"  Incorrecto. La respuesta era: {respuesta}\n")

    print(f"  Resultado: {correctas} / 10")
    if correctas == 10:
        print("  Perfecto! Puntaje maximo!")
    elif correctas >= 7:
        print("  Muy bien!")
    elif correctas >= 5:
        print("  Pasable.")
    else:
        print("  A estudiar un poco mas...")
    return f"{correctas}/10 correctas"

# ─────────────────────────────────────────────
#  JUEGO 5 - Duelo de Dados
# ─────────────────────────────────────────────

def dados():
    print("========================================")
    print("   DUELO DE DADOS")
    print("========================================")
    print("Vos y la PC tiran 3 dados cada uno.")
    print("Gana quien sume mas. 5 rondas.\n")

    semilla = int(input("Ingresa cualquier numero para empezar: "))
    puntos_j = 0
    puntos_pc = 0

    for ronda in range(1, 6):
        print(f"\n  -- Ronda {ronda}/5 --")
        input("  Presiona ENTER para tirar los dados...")

        d1 = (semilla + ronda * 7)  % 6 + 1
        d2 = (semilla + ronda * 13) % 6 + 1
        d3 = (semilla + ronda * 19) % 6 + 1
        suma_j = d1 + d2 + d3

        p1 = (semilla + ronda * 11) % 6 + 1
        p2 = (semilla + ronda * 17) % 6 + 1
        p3 = (semilla + ronda * 23) % 6 + 1
        suma_pc = p1 + p2 + p3

        print(f"  Tus dados:    {d1}  {d2}  {d3}  -> suma: {suma_j}")
        print(f"  Dados de PC:  {p1}  {p2}  {p3}  -> suma: {suma_pc}")

        if suma_j > suma_pc:
            print("  Ganaste la ronda!")
            puntos_j += 1
        elif suma_pc > suma_j:
            print("  Gano la PC.")
            puntos_pc += 1
        else:
            print("  Empate.")

    print(f"\n  Resultado final -> Vos: {puntos_j}  |  PC: {puntos_pc}")
    if puntos_j > puntos_pc:
        print("  Ganaste el duelo!")
        return f"gano {puntos_j}-{puntos_pc}"
    elif puntos_pc > puntos_j:
        print("  Perdiste el duelo.")
        return f"perdio {puntos_j}-{puntos_pc}"
    else:
        print("  Empate total!")
        return f"empate {puntos_j}-{puntos_pc}"

# ─────────────────────────────────────────────
#  PUNTAJES
# ─────────────────────────────────────────────

def guardar_puntaje(usuario, juego, resultado):
    archivo = open("puntajes.txt", "a")
    archivo.write(f"{usuario} | {juego} | {resultado}\n")
    archivo.close()

def ver_puntajes():
    print("========================================")
    print("           TABLA DE PUNTAJES")
    print("========================================")
    try:
        archivo = open("puntajes.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        if lineas:
            for linea in lineas:
                print(f"  {linea}", end="")
        else:
            print("  Todavia no hay puntajes guardados.")
    except:
        print("  Todavia no hay puntajes guardados.")

# ─────────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────────

while True:
    print("\n========================================")
    print(f"     BIENVENIDO, {usuario}!")
    print("========================================")
    print("  1. Adivina el numero")
    print("  2. Piedra, Papel, Tijeras")
    print("  3. Mayor o Menor")
    print("  4. Trivia")
    print("  5. Duelo de Dados")
    print("  6. Ver puntajes")
    print("  0. Salir")
    print("========================================")

    opcion = input("\n  Elegi una opcion: ")

    if opcion == "0":
        break
    elif opcion == "1":
        resultado = adivina_numero()
        guardar_puntaje(usuario, "Adivina el numero", resultado)
    elif opcion == "2":
        resultado = piedra_papel_tijeras()
        guardar_puntaje(usuario, "Piedra Papel Tijeras", resultado)
    elif opcion == "3":
        resultado = mayor_o_menor()
        guardar_puntaje(usuario, "Mayor o Menor", resultado)
    elif opcion == "4":
        resultado = trivia()
        guardar_puntaje(usuario, "Trivia", resultado)
    elif opcion == "5":
        resultado = dados()
        guardar_puntaje(usuario, "Duelo de Dados", resultado)
    elif opcion == "6":
        ver_puntajes()
        opcion = "x"
    else:
        print("  Opcion invalida.")
        opcion = "x"

    if opcion != "x":
        print("\n  Puntaje guardado!")
        print("  M - Volver al menu  |  0 - Salir")
        accion = input("  Tu eleccion: ")
        if accion != "M" and accion != "m":
            break

print(f"\n  Hasta luego, {usuario}!\n")
