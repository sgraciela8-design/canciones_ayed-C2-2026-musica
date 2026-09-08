import click
import tabulate

lista_canciones = [
    {"id": 1, "Titulo": "Crimen", "Artista": "Gustavo Cerati","Album": "Fuerza natural"},
    {"id": 2, "Titulo": "Adios", "Artista": "Gustavo Cerati", "Album": "Fuerza natural"},
    {"id": 3, "Titulo": "Here Comes the Sun", "Artista": "The Beatles": "Album": "Abbey Road"},
]

def listar_canciones():
    for item in lista_canciones:
        print (f"{item['id']: >2} {item ['Titulo']}")