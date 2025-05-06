def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """
    Esta funcion recibe por parametro una cadena de caracteres (piedra, papel o tijera) y determina si el jugador o la maquina es ganadora.
    Args:
        jugador (int): Eleccion del jugador (1 para Piedra, 2 para Papel, 3 para Tijera).
        maquina (int): Eleccion de la maquina (1 para Piedra, 2 para Papel, 3 para Tijera).
    Returns:
        str: Devuelve "jugador" si el jugador gana la ronda, 
        "Maquina" si la maquina gana la ronda y 
        "Empate" si ambos eligen el mismo elemento.
    """
    if jugador == maquina:
        ganador = "Empate"
        
    else:
        if (maquina == 1 and jugador == 3) or (maquina == 3 and jugador == 2) or (maquina == 2 and jugador == 1):
            ganador = "Maquina"
        
        if (jugador == 1 and maquina == 3) or (jugador == 3 and maquina == 2) or (jugador == 2 and maquina == 1):
            ganador = "Jugador"

    return ganador

def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """
    Esta funcion recibe por parametro una cadena de caracteres (piedra, papel o tijera) y determina si el jugador o la maquina es ganadora.
    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.
        ronda_actual (int): Número de la ronda actual.
    Returns:
        bool: Devuelve True -> si la partida sigue en curso, Devuelve False -> si la partida ha finalizado 
        (porque alguien gano 2 veces seguidas o se jugaron todas las rondas).
    """
    bandera = True
    if aciertos_jugador == 2 or aciertos_maquina == 2 or ronda_actual == 3:
        bandera = False
    
    return bandera

def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """
    Esta funcion recibe por parametro los aciertos de cada jugador y determina cual es el ganador de la partida.
    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.
    Returns:
        str: Devuelve "Jugador" Si gana la partida el jugador, Devuelve "Maquina" si gana la partida la maquina.
    """
     
    if aciertos_jugador == 2 or aciertos_jugador > aciertos_maquina:
        ganador = "Jugador"
    
    if aciertos_maquina == 2 or aciertos_maquina > aciertos_jugador:
        ganador = "Maquina"
        
    return ganador