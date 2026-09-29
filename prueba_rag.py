from rag import buscar_contexto

consulta = """
El servidor se está quedando sin espacio.
El almacenamiento está casi lleno y no puede guardar archivos.
"""

resultados = buscar_contexto(
    consulta,
    cantidad=3
)


print("\n=== FRAGMENTOS RECUPERADOS ===\n")


for resultado in resultados:

    print("Archivo:", resultado["archivo"])

    print(
        "Fragmento:",
        resultado["fragmento"]
    )

    print(
        "Similitud:",
        round(resultado["similitud"], 3)
    )

    print("Contenido:")
    print(resultado["contenido"])

    print("\n----------------------------\n")
