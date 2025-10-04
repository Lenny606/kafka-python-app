import json
import random
import uuid

from confluent_kafka import Producer

# defining Producer, and where is Kafka accesible
producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

def delivery_report(err,msg):
    if err:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}] with Data {}'.format(msg.topic(), msg.value(), dir(msg)))

producer = Producer(producer_config)

# mock data
order = {
    'order_id': str(uuid.uuid4()),
    'user': "user_name",
    "item": "item_name",
    'quantity': random.randint(1, 8)
}

# encode dict into byte format json representation
value = json.dumps(order).encode('utf-8')

# send to topic (if  not exists it will be created), add callback for monitor
producer.produce(topic='orders', value=value, callback=delivery_report)

# events are buffered and send in batches
producer.flush()