from abstract_products import Boton  # Importamos la clase abstracta Boton

# Implementación concreta de Boton para Mac
class BotonMac(Boton):
    def renderizar(self):
        return "Renderizando Botón Mac"  # Especificación de la representación del botón en Mac
