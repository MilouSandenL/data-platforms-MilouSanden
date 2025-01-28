from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"

# reads in jokes.json - genom sin absoluta väg(data_path)
with open(data_path / "jokes.json", "r") as file:
     jokes = json.load(file)
     
# pprint(jokes)

# entry - point för att integrera med kafka (med hjälp av application)
# 9092 är vår localhost för port mapped for broker container. - för att kunna prata med brokern. (fungerar bara om man har brokern (server) öppen)
app = Application(broker_address="localhost:9092", consumer_group="text_splitter")

# vi gör om datan till binary för att skicka den till topicen. json objektet görs om till ett format som vi kan skicka vidare.
jokes_topic = app.topic(name= "jokes", value_serializer="json")
# print(jokes_topic)

# detta skapar vår producer -> app.producer.
def main():
    with app.get_producer() as producer:
        # print(producer)

# loopar igenom jokes (som är en dictionary) - serializerar så vi får ett kafka meddelande
        for joke in jokes:
            
            kafka_msg = jokes_topic.serialize(key = joke["joke_id"], value = joke)
            
            print(f"Produced message: key = {kafka_msg.key}, value = {kafka_msg.value}")
# lägger in nyckel och värde för att skapa topic.
            producer.produce(
                topic = "jokes", key = str(kafka_msg.key), value = kafka_msg.value
            )

# den här koden körs när man exikuverar scriptet och inte när man importerar moduler
# används för att säkerställa att det ska köras som eget skript, om man skulle försöka importera detta script.
if __name__ == '__main__':
    pprint(jokes)
    main()