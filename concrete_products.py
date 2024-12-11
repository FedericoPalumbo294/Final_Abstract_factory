# Definir las implementaciones concretas de los productos abstractos
from abstract_products import Boton  # Importar la clase Boton

# Implementación concreta de Boton para Mac
class BotonMac(Boton):
    def renderizar(self):
        return "Renderizando Botón Mac"

# Implementación concreta de Boton para Windows
class BotonWindows(Boton):
    def renderizar(self):
        return "Renderizando Botón Windows"
