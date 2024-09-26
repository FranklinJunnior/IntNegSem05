import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Gestion argumentos desde la línea de comandos")

# Agregar el argumento --nombre
parser.add_argument("--nombre", help="Tu nombre", default="Mundo")

# Parsear los argumentos
args = parser.parse_args()

# Imprimir el saludo
print(f'Hola {args.nombre}')
