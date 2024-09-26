import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer

# Configuración del productor de Kafka
kafka_producer = KafkaProducer(bootstrap_servers='localhost:29092')

# Enviar un mensaje al tópico 'prueba_topico'
kafka_producer.send('prueba_topico', key=b'key', value=b'Mensaje Enviado')

# Asegurarse de que todos los mensajes sean enviados
kafka_producer.flush()

# Cerrar el productor
kafka_producer.close()
