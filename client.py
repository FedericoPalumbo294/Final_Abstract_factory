# Cliente que usa la fábrica para crear y renderizar botones

def renderizar_interfaz(fabrica):
    # Usa la fábrica para crear un botón
    boton = fabrica.crear_boton()
    # Llama al método renderizar del botón creado y lo muestra
    print(boton.renderizar())
