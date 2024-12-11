from abstract_factory import FabricaGUI  # Importamos la clase FabricaGUI
from boton_windows import BotonWindows  # Importamos la clase BotonWindows

# Fábrica concreta para crear botones Windows
class FabricaWindows(FabricaGUI):
    def crear_boton(self):
        return BotonWindows()  # Retorna una instancia de BotonWindows
