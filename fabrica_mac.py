from abstract_factory import FabricaGUI  # Importamos la clase FabricaGUI
from boton_mac import BotonMac  # Importamos la clase BotonMac

# Fábrica concreta para crear botones Mac
class FabricaMac(FabricaGUI):
    def crear_boton(self):
        return BotonMac()  # Retorna una instancia de BotonMac
