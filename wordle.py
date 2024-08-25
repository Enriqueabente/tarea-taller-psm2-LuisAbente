import random
from termcolor import colored

def obtener_palabra_secreta():
    """
    Función para seleccionar una palabra secreta al azar de una lista predefinida.
    """
    palabras = ["pyton", "juego", "labra", "azar", "texto", "color"]
    return random.choice(palabras)

def obtener_entrada_usuario():
    """
    Función para obtener la entrada del usuario y asegurarse de que sea válida.
    """
    while True:
        entrada = input(colored("Introduce tu conjetura de 5 letras: ", "blue")).lower()
        if len(entrada) == 5 and entrada.isalpha():
            return entrada
        else:
            print(colored("Por favor, introduce exactamente 5 letras.", "red"))

def comparar_palabras(palabra_secreta, conjetura):
    """
    Función para comparar la palabra secreta con la conjetura del usuario.
    Retorna una cadena que indica las letras en posiciones correctas, incorrectas o faltantes.
    """
    resultado = ""
    for i in range(len(palabra_secreta)):
        if i < len(conjetura):  # Asegurar que hay letras suficientes en la conjetura
            if palabra_secreta[i] == conjetura[i]:
                resultado += colored(conjetura[i], "green")
            elif conjetura[i] in palabra_secreta:
                resultado += colored(conjetura[i], "yellow")
            else:
                resultado += conjetura[i]
        else:
            resultado += "_"
    return resultado

def jugar_wordle():
    """
    Función principal para jugar Wordle.
    """
    palabra_secreta = obtener_palabra_secreta()
    intentos_restantes = 5
    while intentos_restantes > 0:
        print(colored("\nIntentos restantes:", "blue"), intentos_restantes)
        conjetura = obtener_entrada_usuario()
        resultado = comparar_palabras(palabra_secreta, conjetura)
        print(colored("Resultado:", "blue"), resultado)
        if resultado == colored("", "green") * 5:
            print(colored("¡Felicidades! Has adivinado la palabra secreta:", "green"), palabra_secreta)
            return
        intentos_restantes -= 1
    print(colored("Lo siento, has agotado tus intentos. La palabra secreta era:", "red"), palabra_secreta)

# Comienza
print(colored("¡Bienvenido a Wordle!", "magenta"))
print(colored("Intenta adivinar la palabra secreta de 5 letras.", "magenta"))
jugar_wordle()

# Opción para volver a jugar
while True:
    volver_a_jugar = input(colored("¿Quieres volver a jugar? (s/n): ", "blue")).lower()
    if volver_a_jugar == "s":
        print(colored("¡Comencemos de nuevo!", "magenta"))
        print(colored("Intenta adivinar la palabra secreta de 5 letras.", "magenta"))
        jugar_wordle()
    elif volver_a_jugar == "n":
        print(colored("Gracias por jugar. ¡Hasta luego!", "magenta"))
        break
    else:
        print(colored("Por favor, introduce 's' para jugar de nuevo o 'n' para salir.", "red"))
