import subprocess

resultado = subprocess.run(['echo', 'Hola Franklin'], capture_output=True, shell=True)
print(resultado.stdout.decode())
