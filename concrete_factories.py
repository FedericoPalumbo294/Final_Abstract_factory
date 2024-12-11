from abstract_factory import FabricaGUI  # Importar la clase FabricaGUI
from concrete_products import BotonMac, BotonWindows  # Importar los botones concretos

# Fábrica concreta para crear botones Mac
class FabricaMac(FabricaGUI):
    def crear_boton(self):
        return BotonMac()

# Fábrica concreta para crear botones Windows
class FabricaWindows(FabricaGUI):
    def crear_boton(self):
        return BotonWindows()
