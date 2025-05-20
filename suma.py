from logger_config  import get_logger


logger = get_logger('suma')
def suma(a,b):

    try:
        resultado = a + b
        logger.info(f"suma. {a} + {b} = {resultado}")
        return resultado
    except TypeError as e:
        logger.error(f"Error al sumar: a={a},  b={b} -> {e}")
        return None






