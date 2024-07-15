import traceback
import logging

logging.basicConfig(
    filename="6\execution.log",
    level = logging.ERROR
)
logger = logging.getLogger("Delivery")


class CantidadInvalidaError(Exception):
    def __init__(self):
        self.message = "Error al registrar la cantidad de pizzas y/o comensaales"
        super().__init__(self.message)
    
class NoRegistraComensalesError(Exception):
       def __init__(self):
        self.message = "Parece que nadie quiere pizza :("
        super().__init__(self.message)
       
        
def dividir_pizzas(pizzas: int, comensales: int)->float:    #versión buenas prácticas
    '''
    Función para dividir en porciones las pizzas
    '''
    
    logger.info(f"Nuevo pedido de {pizzas} pizzas para {comensales} personas")
    try:
        if not (type(pizzas) | type(comensales)) in (int, float):
           raise CantidadInvalidaError 
        if comensales == 0:
            raise NoRegistraComensalesError
        porciones = pizzas/comensales
        
        logger.info(f"El pedido es de {pizzas} pizzas, cada comensal puede comer {porciones} /pizza")
        
    except (CantidadInvalidaError, NoRegistraComensalesError) as e:
        logger.error(f"Error al recibir el pedido: {e.message}")
    except Exception as e:
        logger.error(f"Error desconocido al recibir el pedido:\n")
        logger.error(traceback.format_exc())
        
    else:   #el else se usa muy poco
        logger.info("El pedido se recibió correctamente")
        
    finally:
        logger.info("Pedido finalizado")


dividir_pizzas(10, 5)