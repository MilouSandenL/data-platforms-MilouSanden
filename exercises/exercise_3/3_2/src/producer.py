from pathlib import Path
import json
from quixstreams import Application
from pprint import pprint

# Data-mappen är i 3_1/data
data_path = Path(__file__).parents[1] / "data"

# Läs in order.json
with open(data_path / "order.json", "r") as file:
    orders = json.load(file)

# Skapar en Kafka-producent
app = Application(broker_address="localhost:9092", consumer_group="order_group")

# Skapa en Kafka-topic för orders
order_topic = app.topic(name="orders_topic", value_serializer="json")

# Producerar meddelanden till Kafka
def main():
    with app.get_producer() as producer:
        for order in orders:
            kafka_msg = order_topic.serialize(key=order["order_id"], value=order)
            print(f"Producerat meddelande: key = {kafka_msg.key}, value = {kafka_msg.value}")
            
            producer.produce(
                topic="orders_topic",
                key=str(kafka_msg.key),
                value=kafka_msg.value
            )

# Kör producenten
if __name__ == '__main__':
    pprint(orders)
    main()



