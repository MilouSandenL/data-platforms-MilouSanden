# producern skickar data (meddelanden) till kafka. 
from pathlib import Path
import json
from quixstreams import Application
from pprint import pprint

# vägen (pathen) där order.json ligger. Path(__file__) ger den nuvarande filens sökväg, .parten[1] går upp ett steg för att komma till den överordnade mappen. (data)
data_path = Path(__file__).parents[1] / "data"

# öppnar filen order.json och läser den med hjälp av 'r', sparar i variabel file. läser in den med ett python-objekt (orders) med hjälp av json.load()
with open(data_path / "order.json", "r") as file:
    orders = json.load(file)

# Skapar en kafka applikation som skickar data till kafka-brokern på localhost:9092.
# brokern är den server som hanterar alla dataflöden. Definierar en consumer group (används när man vill ha olika consumers som prenumererar på samma topic)
app = Application(broker_address="localhost:9092", consumer_group="order_group")

# definierar kafka-topic med namnet 'order_topic' - value_serializer används för att tala om att datan ska skickas som JSON.
order_topic = app.topic(name="orders_topic", value_serializer="json")

# Funktion för producer logiken körs. 
def main():
# skapar en producer som kan skriva data till kafka med hjälp av app.get_producer()
    with app.get_producer() as producer:
# loopar igenom varje order i json-filen och skapar ett meddelande som skickas till kafka.
        for order in orders:
# skapar ett kafka-meddelande där varje order är omvandlade till ett format som kafka kan skicka. nyckeln är order_id och värder är hela orderonjektet i jsonfilen.
            kafka_msg = order_topic.serialize(key=order["order_id"], value=order)
            print(f"Producerat meddelande: key = {kafka_msg.key}, value = {kafka_msg.value}")
# skickar meddelandet till kafka med .produce() - meddelandet som är producerat skickas till topicen order_topics.
            producer.produce(
                topic="orders_topic",
                key=str(kafka_msg.key),
                value=kafka_msg.value
            )

# Kör producenten
if __name__ == '__main__':
    pprint(orders)
    main()



