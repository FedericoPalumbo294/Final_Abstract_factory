from fabrica_mac import FabricaMac  # Importamos la fábrica para Mac
from fabrica_windows import FabricaWindows  # Importamos la fábrica para Windows
from client import renderizar_interfaz  # Importamos la función que renderiza la interfaz

# Uso
renderizar_interfaz(FabricaMac())      # Llama a la función con la fábrica de Mac
renderizar_interfaz(FabricaWindows())  # Llama a la función con la fábrica de Windows
