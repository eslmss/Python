import logging
import traceback

logging.basicConfig(
    filename=r"6\4.ejercicio_execution.log",
    level = logging.INFO,    #ahora solo dice INFO, puede ser ERROR, etc (¿habría que agregar más objetos logging?)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Agrega %(asctime)s para la hora
)
logger = logging.getLogger("Ejercicio")

class PosicionExcedeAlTexto(Exception): #IndexError
    def __init__(self):
        self.message = "La posicion indicada no esta dentro del texto enviado"
        super().__init__(self.message)
        
class IngresosInvalidos(Exception): #TypeError
    def __init__(self):
        self.message = "Error al registrar el texto y/o su posicion"
        super().__init__(self.message)


def ubicar_char(texto:str, num:int)->str:
    '''
    Función que recibe un string y retorna el char de una posicion especificada
    '''
    
    logger.info(f"En el texto '{texto}', se ubicara el caracter en la posicion: {num}")
    try:
        if (type(texto) != str) | (type(num) != int):
            raise IngresosInvalidos
        if (num > (len(texto)-1)) | (num<0):
            raise PosicionExcedeAlTexto
        logger.info(f"En el texto '{texto}', el caracter en la posicion '{num}' es -----> {texto[num]}")
        
    except (IngresosInvalidos, PosicionExcedeAlTexto) as e:
        logger.error(f"Algo salio mal: {e.message}")
    except Exception as e:  #Error Desconocido
        logger.error(f"Error desconocido al recibir los datos\n")
        logger.error(traceback.format_exc())
        
    else: # se usa poco
        logger.info("Los datos se recibieron correctamente") 
    finally:
        logger.info("Ejercicio finalizado") 
        
ubicar_char("Elias", -4)
