from river import anomaly

# Crear un modelo de detección de anomalías
modelo = anomaly.OneClassSVM(nu=0.1)

# Datos de ejemplo
datos = [
    {'feature1': 1, 'feature2': 2},
    {'feature1': 2, 'feature2': 3},
    {'feature1': 3, 'feature2': 4},
    {'feature1': 100, 'feature2': 200}  # Anomalía
]

# Definir un umbral para la detección de anomalías
umbral = 0.5

# Entrenar el modelo y detectar anomalías
for x in datos:
    score = modelo.score_one(x)
    es_anomalia = score > umbral
    print(f"Datos: {x}, Anomalía: {es_anomalia}")
    modelo.learn_one(x)
