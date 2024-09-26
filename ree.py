import re

texto = "Mi número es 123-456-7890"
resultado = re.search(r'\d{5}-\d{3}-\d{4}', texto)

if resultado:
    print("Número de teléfono encontrado:", resultado.group())
else:
    print("No se encontró ningún número de teléfono.")
