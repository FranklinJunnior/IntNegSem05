import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves
    
from kafka import KafkaConsumer

# Configuración del consumidor de Kafka
kafka_consumer = KafkaConsumer(
    'prueba_topico',
    bootstrap_servers='localhost:29092',
    group_id='mi_grupo',
)

# Imprimir los mensajes del tópico
for mensaje in kafka_consumer:
    print(f"Clave: {mensaje.key}, Valor: {mensaje.value}")

# Cerrar el consumidor
kafka_consumer.close()
