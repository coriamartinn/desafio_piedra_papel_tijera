import random
from paquetes.elecciones import mostrar_elemento
from paquetes.validates import validate_int
from paquetes.verificaciones import verificar_ganador_ronda, verificar_estado_partida, verificar_ganador_partida


def jugar_piedra_papel_tijera() -> str:
    """
    Funcion main, donde se llama para comenzar la partida y ejecutar cada proceso modularizado.
    Args:
    No recibe argumentos.
    Returns:
        str: Retorna el comienzo del juego y cada llamado y ejecucion de las demas funciones.
    """
    
    contador_maquina = 0
    contador_jugador = 0
    contador_rondas = 0
    
    while contador_rondas < 3 or (contador_maquina < 2 and contador_jugador < 2):
        # eleccion maquina
        eleccion_maquina = random.randint(1, 3)

        # eleccion del jugador
        eleccion_jugador = input(
            "Ingrese que quiere jugar (1 = Piedra, 2 = Papel, 3 = Tijera): ")
        # validamos la eleccion del jugador
        validacion = validate_int(eleccion_jugador)

        # si el jugador no cumple con la eleccion esperada entramos al bucle
        while not validacion:
            print("Ingresas una eleccion fuera del rango estipulado. realiza de vuelta la eleccion")
            eleccion_jugador = input(
                "Ingrese que quiere jugar (1 = Piedra, 2 = Papel, 3 = Tijera): ")
            validacion = validate_int(eleccion_jugador)

        # preguntamos si validacion da True
        if validacion:
            # parseamos a entero la eleccion
            eleccion_jugador = int(eleccion_jugador)
            # Llamamos a la funcion de mostrar elementos
            jugador = mostrar_elemento(eleccion_jugador)

        maquina = mostrar_elemento(eleccion_maquina)
        print(f"La eleccion del jugador fue: {jugador}")
        print(f"La eleccion de la maquina fue: {maquina}")


        resultado = verificar_ganador_ronda(eleccion_jugador, eleccion_maquina)
        contador_rondas += 1

        if resultado == "Maquina":
            contador_maquina += 1
            print(f"La maquina es la ganadora de la ronda {contador_rondas}")
        else:
            contador_jugador += 1
            print(f"El jugador es el ganador de la ronda {contador_rondas}")
        
            estado_partida = verificar_estado_partida(contador_jugador, contador_maquina, contador_rondas)

    if not estado_partida:
        ganador_partida = verificar_ganador_partida(contador_jugador, contador_maquina)
        print(f"El ganador de la partida es El/La: ")
        return ganador_partida

arturo_jugando = jugar_piedra_papel_tijera()
print(arturo_jugando)
