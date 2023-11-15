from typing import List

class Casilla:
    def __init__(self):
        self.espacio_disp = "   |"
        self.coordenada_x = 0
        self.coordenada_y = 0
        self.estado = 1

class Barco:
    def __init__(self):
        self.casilla_inicial_x = 3
        self.casilla_inicial_y = 3
        self.posicion = 1
        self.numero_casillas = 5
        self.nombre = "portaaviones"
        self.area = []

class Jugador:
    def __init__(self):
        self.flota = []
        self.tablero = []
        self.ataque = []

class Tiro:
    def __init__(self):
        self.coordenadas = Casilla()
        self.resultado = 0

def validar_int(msj):
    while True:
        try:
            valor = int(input(msj))
            if 1 <= valor <= 10:
                return valor
            else:
                print("El dato ingresado no es válido, debe estar entre 1 y 10.")
        except ValueError:
            print("El dato ingresado no es válido, debe ser un número entero entre 1 y 10.")

def validar_int_pos(msj):
    while True:
        try:
            valor = int(input(msj))
            if valor in [0, 1]:
                return valor
            else:
                print("El dato ingresado no es válido, debe ser 0 o 1.")
        except ValueError:
            print("El dato ingresado no es válido, debe ser 0 o 1.")

def validar_str(msj):
    while True:
        valor = input(msj).upper()
        if "A" <= valor <= "J" and len(valor) == 1:
            return ord(valor) - 65
        else:
            print("El dato ingresado no es válido, debe ser una letra de la A a la J.")

def dibujar_cuadricula(casilla_list):
    agua2 = "___|"

    for i in range(10):
        print(f"   {i + 1}", end=" ")

    print("\n  ", end=" ")
    for i in range(10):
        print("___ ", end=" ")

    for valor in range(65, 75):
        letra = chr(valor)
        print(f"\n{letra}|", end=" ")
        for i in range(1, 11):
            espacio = False
            for casilla in casilla_list:
                if casilla.coordenada_y == (valor - 65) and casilla.coordenada_x == i:
                    print(casilla.espacio_disp, end="")
                    espacio = True
                    break
            if not espacio:
                print("   |", end=" ")

    print()

def dibujar_tiro(tiro, casilla_list2):
    print("dibujando..")
    casilla_list = []

    if tiro.resultado == 1:
        print("tiro acertado..")
        casilla = Casilla()
        casilla.coordenada_x = tiro.coordenadas.coordenada_x
        casilla.coordenada_y = tiro.coordenadas.coordenada_y
        casilla.espacio_disp = " X |"  # Cambiado a 'X' para indicar un acierto
        casilla.estado = 2

        casilla_list.append(casilla)

    elif tiro.resultado == 0:
        print("tiro fallido..")
        casilla1 = Casilla()
        casilla1.coordenada_x = tiro.coordenadas.coordenada_x
        casilla1.coordenada_y = tiro.coordenadas.coordenada_y
        casilla1.espacio_disp = " - |"  # Cambiado a '-' para indicar un fallo
        casilla1.estado = 3

        casilla_list.append(casilla1)

    elif tiro.resultado == 2:
        print("Hundiste un barco..")
        casilla2 = Casilla()
        casilla2.coordenada_x = tiro.coordenadas.coordenada_x
        casilla2.coordenada_y = tiro.coordenadas.coordenada_y
        casilla2.espacio_disp = " @ |"
        casilla2.estado = 4

        casilla_list.append(casilla2)

    print(len(casilla_list))
    return casilla_list


def resultado_tiro(tiro, jugador, jugador_oponente):
    res = 0
    tiros_barco = []

    for tiro1 in jugador.ataque:
        tiros_barco.append(tiro1.coordenadas)

    for casilla_barco in jugador_oponente.flota:
        if any(casilla.coordenada_x == tiro.coordenadas.coordenada_x and casilla.coordenada_y == tiro.coordenadas.coordenada_y for casilla in casilla_barco.area):
            tiros_barco.append(tiro.coordenadas)
            if len(casilla_barco.area) - len(list(filter(lambda x: x in tiros_barco, casilla_barco.area))) == 0:
                res = 2
            else:
                res = 1

    tiro.resultado = res
    return tiro

def dibujar_barco(barco, casilla_list2):
    casilla_list = []

    if barco.posicion == 0:
        for y in range(barco.casilla_inicial_y, barco.casilla_inicial_y + barco.numero_casillas):
            casilla = Casilla()
            casilla.coordenada_x = barco.casilla_inicial_x
            casilla.coordenada_y = y
            casilla.espacio_disp = " B |"
            casilla.estado = 1

            casilla_list.append(casilla)
    else:
        for x in range(barco.casilla_inicial_x, barco.casilla_inicial_x + barco.numero_casillas):
            casilla = Casilla()
            casilla.coordenada_y = barco.casilla_inicial_y
            casilla.coordenada_x = x
            casilla.espacio_disp = " B |"
            casilla.estado = 1

            casilla_list.append(casilla)

    duplicates = [item for item in casilla_list2 if item in casilla_list]

    for lista in duplicates:
        print(any(duplicates))

    if duplicates:
        print("CHOCA CON OTRO BARCO, ESCRIBE NUEVAS COORDENADAS")
        return solicitar_coordenadas(barco.nombre, casilla_list2)
    else:
        barco.area.extend(casilla_list)
        return barco

def solicitar_coordenadas(nombre, casilla_list2):
    barco = Barco()
    print("for dentro")

    if nombre == "acorazado":
        barco.nombre = nombre
        barco.numero_casillas = 4
    elif nombre == "portaaviones":
        barco.nombre = nombre
        barco.numero_casillas = 5
    elif nombre == "crucero":
        barco.nombre = nombre
        barco.numero_casillas = 1
    elif nombre == "submarino":
        barco.nombre = nombre
        barco.numero_casillas = 3
    elif nombre == "destructor":
        barco.nombre = nombre
        barco.numero_casillas = 2

    casilla_list = []

    barco.nombre = nombre

    print(f"\n\n{barco.nombre.upper()}: {barco.numero_casillas} casillas\n\n")

    barco.posicion = validar_int_pos("Ingrese si su barco estará en Vertical, escriba 0, o si estará en horizontal escriba 1")
    barco.casilla_inicial_x = validar_int("Ingrese coordenada numérica en la que iniciará las dimensiones de su barco del 1 al 10")
    barco.casilla_inicial_y = validar_str("Ingrese coordenada Alfanumérica en la que iniciará las dimensiones de su barco, de la A a la J") - 65

    while (barco.casilla_inicial_x + barco.numero_casillas > 10 and barco.posicion == 1) or (barco.casilla_inicial_y + barco.numero_casillas > 10 and barco.posicion == 0):
        barco.casilla_inicial_x = validar_int("LAS CASILLAS NO ESTÁN DISPONIBLES coordenada numérica en la que iniciará las dimensiones de su barco del 1 al 10")
        barco.casilla_inicial_y = validar_str("Ingrese coordenada Alfanumérica en la que iniciará las dimensiones de su barco, de la A a la J") - 65

    barco = dibujar_barco(barco, casilla_list2)

    return barco

def cambiar_espacio(estado):
    mi_casilla = Casilla()

    if estado == 0:
        mi_casilla.espacio_disp = "   |"
    elif estado == 1:
        mi_casilla.espacio_disp = " B |"
    elif estado == 2:
        mi_casilla.espacio_disp = " X |"
    else:
        mi_casilla.espacio_disp = " - |"

def solicitar_tiro(jugador_oponente, jugador):
    tiro = Tiro()
    casilla_list = []

    print("\n\n Elije la casilla a la que enviarás el tiro y escribe las coordenadas \n\n")

    tiro.coordenadas.coordenada_x = validar_int("Ingrese coordenada numérica X")
    tiro.coordenadas.coordenada_y = validar_str("Ingrese coordenada Alfanumérica Y") - 65

    while any(casilla.coordenada_x == tiro.coordenadas.coordenada_x and casilla.coordenada_y == tiro.coordenadas.coordenada_y for casilla in jugador.tablero):
        print("Ya escribió esta coordenada, escriba otra")
        tiro.coordenadas.coordenada_x = validar_int("Ingrese coordenada numérica X")
        tiro.coordenadas.coordenada_y = validar_str("Ingrese coordenada Alfanumérica Y") - 65

    print(f"X{tiro.coordenadas.coordenada_x}")
    print(f"Y{tiro.coordenadas.coordenada_y}")

    tiro.resultado = resultado_tiro(tiro, jugador, jugador_oponente).resultado

    casilla_list.extend(dibujar_tiro(tiro, casilla_list))

    jugador.ataque.append(tiro)
    jugador.tablero.extend(casilla_list)

    return jugador

def main():
    jugador1 = Jugador()
    jugador2 = Jugador()

    print("""
                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                PROYECTO FINAL - BATALLA NAVAL               /
      \                          POR Kevin                        /
       \_________________________________________________________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww 
Instrucciones:
-El objetivo de este juego es hundir los barcos del contrincante, escondidos en alguna parte del tablero de 10 por 10.
-Los barcos tienen diferentes dimensiones, siendo el mas grande de 5 casillas, y el mas pequeño de 1 casilla.
-Para darle a un barco, debes dar las coordenadas 'X' (columna) y 'Y' (fila). 
-Si hay un barco en dicha posición, aparecerá un asterisco (*) en el tablero.
-Si no hay un barco en esa posición, aparecerá una equis (X) en el tablero.
-Para colocar los barcos, solamente debes establecer en que coordenada quieres que este la proa y hacia que direccion (vertical u horizontal).

Por favor, elija una opción:""")

    nombre_barcos = ["portaaviones", "acorazado", "crucero", "submarino", "destructor"]

    casilla_list_tiro1 = []
    casilla_list_tiro2 = []
    casilla_list_flota1 = []
    casilla_list_flota2 = []

    ataque_jugador1 = []
    ataque_jugador2 = []

    jugador1 = Jugador()
    jugador2 = Jugador()

    print('''JUGADOR 1''')

    for i in range(5):
        if len(jugador1.flota) < 1:
            print("for antes")
            jugador1.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota1))
        else:
            jugador1.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota1))
        casilla_list_flota1.extend(jugador1.flota[i].area)
        dibujar_cuadricula(casilla_list_flota1)

    input("Presione cualquier letra para continuar")

    print('''JUGADOR 2''')

    for i in range(5):
        if len(jugador2.flota) < 1:
            jugador2.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota2))
        else:
            jugador2.flota.append(solicitar_coordenadas(nombre_barcos[i], casilla_list_flota2))
        casilla_list_flota2.extend(jugador2.flota[i].area)
        dibujar_cuadricula(casilla_list_flota2)

    input("Presione cualquier letra para continuar")

    print('''EMPIEZA EL JUEGO''')

    while True:
        print('''TURNO JUGADOR 1''')

        jugador1 = solicitar_tiro(jugador2, jugador1)
        dibujar_cuadricula(jugador1.tablero)
        input("Presione cualquier letra para continuar")

        print('''TURNO JUGADOR 2''')

        jugador2 = solicitar_tiro(jugador1, jugador2)
        dibujar_cuadricula(jugador2.tablero)
        input("Presione cualquier letra para continuar")

        if jugador1.ataque.count(lambda tiro: tiro.resultado == 1) >= 15 or jugador2.ataque.count(lambda tiro: tiro.resultado == 1) >= 15:
            break

    if jugador1.ataque.count(lambda tiro: tiro.resultado == 1) > jugador1.ataque.count(lambda tiro: tiro.resultado == 1):
        print('''GANADOR JUGADOR 1''')
    else:
        print('''GANADOR JUGADOR 2''')

if __name__ == "__main__":
    main()


