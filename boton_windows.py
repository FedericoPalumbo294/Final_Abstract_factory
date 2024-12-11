from abstract_products import Boton  # Importamos la clase abstracta Boton

# Implementación concreta de Boton para Windows
class BotonWindows(Boton):
    def renderizar(self):
        return "Renderizando Botón Windows"  # Especificación de la representación del botón en Windows
