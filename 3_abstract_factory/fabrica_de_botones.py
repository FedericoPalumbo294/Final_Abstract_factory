# Abstract Factory
# Ejemplo: Interfaz gráfica para diferentes plataformas.

class Boton: # Clase Boton
    def renderizar(self): # Método renderizar
        pass

class BotonMac(Boton): # Clase BotonMac que hereda de Boton
    def renderizar(self): # Método renderizar
        return "Renderizando Botón Mac"

class BotonWindows(Boton): # Clase BotonWindows que hereda de Boton
    def renderizar(self): # Método renderizar
        return "Renderizando Botón Windows"

class FabricaGUI: # Clase FabricaGUI
    def crear_boton(self): # Método crear_boton
        pass

class FabricaMac(FabricaGUI): # Clase FabricaMac que hereda de FabricaGUI
    def crear_boton(self): # Método crear_boton
        return BotonMac()

class FabricaWindows(FabricaGUI): # Clase FabricaWindows que hereda de FabricaGUI
    def crear_boton(self): # Método crear_boton
        return BotonWindows()

# Uso
def renderizar_interfaz(fabrica): # Función renderizar_interfaz que recibe una fabrica
    boton = fabrica.crear_boton() # Se crea un botón con la fabrica
    print(boton.renderizar())

renderizar_interfaz(FabricaMac())      # "Renderizando Botón Mac"
renderizar_interfaz(FabricaWindows())  # "Renderizando Botón Windows"
