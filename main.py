from alive_progress import alive_bar
import random
import requests, json
import time
import speech_recognition as sr


# Variables para condicionales
seleccion_menu = 0


# Caracteristicas del asistente
nombre_asistente = "Smithers"


# Datos del usuario
nombre_usuario = None
lista_recordatorios = []


# Copy paste de barra de carga
""" with alive_bar(150, bar="bubbles", spinner="arrows") as bar:
    for i in range(150):
        time.sleep(0.01)
        bar() """

# Función sección clima
def ver_clima():
    seguir = ""
    while True:
        time.sleep(1)
        api_key = "72f9b74a4fec68cc95abe733fb6c14e2"
        base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        city_name = input("[+]Ingresá la ciudad: ")
        complete_url = f"{base_url}{city_name}&appid={api_key}"
        response = requests.get(complete_url)
        data = response.json()
        temperature = data["main"]["temp"] - 273.15
        temp_round = round(temperature, 2)
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
            for i in range(100):
                time.sleep(0.01)
                bar()

        try:
            print(
                f"\n[+]La temperatura actual en la ciudad de {city_name.capitalize()} es de {temp_round}°C."
            )
            print(f"[+]La humedad es del {humidity}%")
            print(f"[+]La presión es de {pressure}hPa")
            time.sleep(1)
            seguir = input("\n[+]Deseás hacer otra consulta?y/n : ")
            if seguir.lower() == "n":
                menu()
        except:
            print("\n[+]Ocurrió un error, ingresa nuevamente la ciudad.")


# Funcion de menu
def menu():
    global seleccion_menu
    time.sleep(1)
    print(
        f"\n[+]{nombre_usuario}, estas son algunas de las tareas que puedo hacer por ti : \n"
    )
    print("[1]Recordatorios.")
    print("[2]Clima.")
    print("[3]Juegos.")
    print("[4]Comandos de voz.")
    seleccion_menu = input("\n[+]Seleccioná la opcion con su correspondiente numero : ")
    if seleccion_menu == "1":
        print("\n[+]Seleccionaste la opcion 1\n")
        recordatorios()
    elif seleccion_menu == "2":
        print("\n[+]Seleccionaste la opcion 2\n")
        ver_clima()
    elif seleccion_menu == "3":
        jugar()
    elif seleccion_menu == "4":
        reconocimiento_voz()


# Funcion de recordatorios
def recordatorios():
    seleccion_recordatorio = 0
    while True:
        time.sleep(1)
        print("\n[1]Consultar recordatorios.")
        print("[2]Agregar recordatorios.")
        print("[3]Eliminar recordatorios.")
        print("[4]Volver al menu.")
        seleccion_recordatorio = input(
            "\n[+]Seleccioná la opcion con su correspondiente numero : "
        )
        # Condicionales recordatorio
        if seleccion_recordatorio == "1":
            consulta_recordatorio()
        elif seleccion_recordatorio == "2":
            alta_recordatorio()
        elif seleccion_recordatorio == "3":
            baja_recordatorio()
        elif seleccion_recordatorio == "4":
            menu()
        else:
            print("\n[+]Opcion inexistente.")


# SubFunciones de recordatorios
def consulta_recordatorio():
    numeracion_lista = 1
    time.sleep(1)
    print("\n[+]Seleccionaste la opcion 1.\n")
    if lista_recordatorios == []:
        print("[+]No tenés registrado ningún recordatorio.")
    else:
        print("[+]Estos son tus recordatorios actuales : ")
        for recordatorio in lista_recordatorios:
            print(f"[{numeracion_lista}]{recordatorio}")
            numeracion_lista += 1


def alta_recordatorio():
    time.sleep(1)
    print("\n[+]Seleccionaste la opcion 2.\n")
    while True:
        lista_recordatorios.append(input("[+]Escribe tu recordatorio : "))
        with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
            for i in range(100):
                time.sleep(0.01)
                bar()
        print("\n[+]Recordatorio agregado exitosamente!")
        time.sleep(1)
        entrada = input("\n[+]Te gustaria agregar otro recordatorio? (Si/No) : ")
        if entrada.lower() == "no":
            break
        elif entrada.lower() == "si":
            time.sleep(1)
            print("\n[+]Entendido!")
            time.sleep(1)
        else:
            time.sleep(1)
            print("\n[+]Opcion inexistente.")
            time.sleep(1)
            break


def baja_recordatorio():
    numeracion_lista = 1
    time.sleep(1)
    print("\n[+]Seleccionaste la opcion 1.\n")
    print("[+]Estos son tus recordatorios actuales :")
    for recordatorio in lista_recordatorios:
        print(f"[{numeracion_lista}]{recordatorio}")
        numeracion_lista += 1
    lista_recordatorios.pop(
        int(
            input("\n[+]Selecciona con su numero el recordatorio que desea eliminar : ")
        )
        - 1
    )
    with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()
    print(f"[+]Eliminaste el recordatorio exitosamente!")
    time.sleep(1)


# Función de reconocimiento de voz
def reconocimiento_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold()
        print("[+]YA PUEDES HABLAR! Dime algo!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-MX")
        print(f"[+]Dijiste >>> {text.lower()} <<<")
        time.sleep(1.5)
        if text.lower() == "abrir opcion dos" or text.lower() == "ver clima":
            ver_clima()
        elif text.lower() == "abrir opcion uno" or text.lower() == "ver recordatorios":
            recordatorios()
        elif text.lower() == "abrir opcion tres" or text.lower() == "ver juegos":
            jugar()
    except:
        print("[+]Lo siento, no puedo entenderte.")
        time.sleep(1.5)


# Función juego Piedra Papel Tijera
def jugar_ppt():
    time.sleep(1)
    # Creo lista de opciones del juego
    game_list = ["piedra", "papel", "tijera"]

    # asigno un elemento de manera aleatoria
    computer = game_list[random.randint(0, 2)]

    # setteo jugador a False
    player = False
    with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()
    print("\n[+]Bienvenid@ al Piedra, Papel o Tijera... A jugar!")
    time.sleep(1)
    while player == False:
        # setteo jugador a True
        player = input("\n[+]Piedra, Papel o Tijera?: ")
        if player.lower() == computer:
            print(f"\n[+]Yo también elegí {computer.capitalize()}. Es un Empate!")
            volver = input("\n[+]Querés volver a intentarlo?y/n : ")
            if volver.lower() == "n":
                jugar()
        elif player.lower() == "piedra":
            if computer == "papel":
                print(f"\n[+]Yo elegí {computer.capitalize()}. Perdiste! :(")
                volver = input("\n[+]Querés volver a intentarlo?y/n : ")
                if volver.lower() == "n":
                    jugar()
            else:
                print(f"\n[+]Yo elegí {computer.capitalize()}. Me Ganaste! :)")
                volver = input("\n[+]Querés volver a intentarlo?y/n : ")
                if volver.lower() == "n":
                    jugar()
        elif player.lower() == "papel":
            if computer == "tijera":
                print(f"\n[+]Yo elegí {computer.capitalize()}. Perdiste! :(")
                volver = input("\n[+]Querés volver a intentarlo?y/n : ")
                if volver.lower() == "n":
                    jugar()
            else:
                print(f"\n[+]Yo elegí {computer.capitalize()}. Me Ganaste! :)")
                volver = input("\n[+]Querés volver a intentarlo?y/n : ")
                if volver.lower() == "n":
                    jugar()
        elif player.lower() == "tijera":
            if computer == "piedra":
                print(f"\n[+]Yo elegí {computer.capitalize()}. Perdiste! :(")
                volver = input("\n[+]Querés volver a intentarlo?y/n : ")
                if volver.lower() == "n":
                    jugar()
            else:
                print(f"\n[+]Yo elegí {computer.capitalize()}. Me Ganaste! :)")
                volver = input("\n[+]Querés volver a intentarlo?y/n : ")
                if volver.lower() == "n":
                    jugar()
        else:
            print("\n[+]Mmmhh parece que tipeaste mal, volvé a ingresar una opción!")
        player = False
        computer = game_list[random.randint(0, 2)]


# Función juego adivinar
def adivinar_numero():
    time.sleep(1)
    with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()
    print("\n[+]Bienvenid@! A jugar...!")
    time.sleep(1)
    while True:
        numero_aleatorio = random.randint(1, 100)
        numero_elegido = int(input("\n[+]Elige un número entre el 1 y el 100 : "))

        while numero_elegido != numero_aleatorio:
            if numero_elegido < numero_aleatorio:
                print("\n[+]Busca un número mayor")
            else:
                print("\n[+]Busca un número menor")
            numero_elegido = int(input("\n[+]Elige otro número : "))

        print("\n[+]Ganaste!")
        time.sleep(1)
        continuar = input("\n[+]Querés seguir adivinando?y/n : ")
        if continuar.lower() == "n":
            jugar()


# Función de acceso a los juegos


def jugar():
    with alive_bar(100, bar="bubbles", spinner="arrows") as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()
    while True:

        print("======================================")
        print("========== Lista de Juegos ===========")
        print("=                                    =")
        print("=    [1] +Piedra, Papel o Tijera     =")
        print("=    [2] +Adivinar el número         =")
        print("=    [3] +Volver al menú             =")
        print("=                                    =")
        print("======================================")
        print("======================================")
        juego = input("\n[+]A qué juego querés jugar? : ")

        if juego == "1":
            jugar_ppt()
        elif juego == "2":
            adivinar_numero()
        elif juego == "3":
            menu()
        else:
            print("\n[+]Opcion inexistente.")


# Mensaje de bienvenida
print("---" * 23)
print(f"\n[+]Hola! Soy tu asistente virtual, {nombre_asistente}.")
time.sleep(2)
nombre_usuario = input("[+]Cual es tu nombre? : ")

# Ejecucion de la funcion menu
menu()
