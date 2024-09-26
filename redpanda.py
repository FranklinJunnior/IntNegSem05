from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('mi_topico', key='key', value='mensaje')
p.flush()