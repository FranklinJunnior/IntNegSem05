import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves
    
from kafka.admin import KafkaAdminClient, NewTopic

# Configuración del cliente de administración de Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers='localhost:29092',
    client_id='test_admin'
)

# Definir un nuevo tópico
nuevo_topico = NewTopic(
    name='nuevo_topico',
    num_partitions=1,
    replication_factor=1
)

# Crear el nuevo tópico
try:
    admin_client.create_topics(new_topics=[nuevo_topico], validate_only=False)
    print("El nuevo tópico ha sido creado exitosamente.")
except Exception as e:
    print(f"Error al crear el tópico: {e}")

# Cerrar el cliente de administración
admin_client.close()
