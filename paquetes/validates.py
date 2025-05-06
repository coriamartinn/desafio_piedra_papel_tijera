def validate_int(eleccion: str) -> bool:
    """
    Esta funcion valida si la eleccion del jugador esta entre los casos posibles en el juego (1, 2 o 3).
    Args:
        eleccion (str): dato pasado por el usuario
    Returns:
        bool: Retorna True si es valida la eleccion, Retorna False si es una eleccion no valida.
    """
    bandera = True

    if ord(eleccion) < 49 or ord(eleccion) > 51:
        bandera = False

    return bandera