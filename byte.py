from bytewax.dataflow import Dataflow
from bytewax.inputs import PartitionedInput
from bytewax.outputs import KafkaOutputConfig, StdOutputConfig
from bytewax.execution import run
from bytewax.window import TumblingWindowConfig, EventClockConfig

# Definir el flujo de datos
flow = Dataflow()

# Configurar la entrada particionada
input_config = PartitionedInput(["mensaje1", "mensaje2", "mensaje3"])

# Configurar las salidas a Kafka y a la salida estándar
kafka_output_config = KafkaOutputConfig(
    brokers="localhost:9092",
    topic="mi_tema"
)
std_output_config = StdOutputConfig()

# Configurar la ventana de tiempo
window_config = TumblingWindowConfig(
    length=10,  # Duración de la ventana en segundos
    clock=EventClockConfig()
)

# Definir la lógica de procesamiento
def process_data(item):
    return item.upper()

# Añadir las operaciones al flujo de datos
flow.input("input", input_config)
flow.map(process_data)
flow.output("kafka_output", kafka_output_config)
flow.output("std_output", std_output_config)

# Ejecutar el flujo de datos
if __name__ == "__main__":
    run(flow)
