def mostrar_elemento(eleccion: int) -> str:
    """
    Esta funcion recibe la eleccion del jugador (1 para piedra, 2 para papel, 3 para tijera) 
    y lo devuelve de forma legible como cadena de caracteres.
    Args:
        eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).
    Returns:
        str: "Piedra" cuando su elección == 1 | "Papel" cuando su elección == 2. | "Tijera" cuando su  elección == 3.
    """
    #variable para cambiar sus valores segun sea el caso y tener un unico retorno.
    casos = None
    
    #condicional para determinar donde va la eleccion del usuario.
    match eleccion:
        case 1:
            casos = "Piedra"
        case 2:
            casos = "Papel"
        case 3:
            casos = "Tijera"
                
    return casos