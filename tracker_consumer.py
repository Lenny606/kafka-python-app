import json

from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': "tracker_group",  # for multiple instances ID
    "auto.offset.reset": "earliest"  # action to do if no offset available, starts reading from earliest
}

tracker = Consumer(consumer_config)
tracker.subscribe(['orders'])

# loop for listening + graceful shutdown (if manually stops script)
try:
    while True:
        msg = tracker.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        value = msg.value().decode('utf-8')
        order = json.loads(value)
        print(f"Received order: {order}")
except KeyboardInterrupt:
   print('Stopping consumer...')
finally:
    tracker.close()