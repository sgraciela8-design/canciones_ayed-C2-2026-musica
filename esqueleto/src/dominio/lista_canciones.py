# Lista de canciones estructurada como un arreglo de diccionarios
canciones = [
    {"id": 1, "titulo": "Creep", "artista": "Radiohead", "album": "Pablo Honey", "anio": 1993},
    {"id": 2, "titulo": "Karma Police", "artista": "Radiohead", "album": "OK Computer", "anio": 1997},
    {"id": 3, "titulo": "Bohemian Rhapsody", "artista": "Queen", "album": "A Night at the Opera", "anio": 1975},
    {"id": 4, "titulo": "Blinding Lights", "artista": "The Weeknd", "album": "After Hours", "anio": 2020},
    {"id": 5, "titulo": "Hotel California", "artista": "Eagles", "album": "Hotel California", "anio": 1976}
]

# Definición del formato de la tabla (los números definen el ancho de cada columna)
# < indica alineación a la izquierda, > a la derecha
formato_fila = "{:<4} | {:<20} | {:<15} | {:<22} | {:<14}"

# 1. Imprimir la primera fila con los títulos de las columnas
print(formato_fila.format("id", "titulo", "artista", "album", "año del album"))

# Imprimir una línea divisoria estética
print("-" * 85)

# 2. Recorrer la lista e imprimir cada canción en formato tabla
for c in canciones:
    print(formato_fila.format(c["id"], c["titulo"], c["artista"], c["album"], c["anio"]))

