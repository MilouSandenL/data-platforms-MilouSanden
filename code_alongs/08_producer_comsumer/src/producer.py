from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"


with open(data_path / "jokes.json", "r") as file:
     jokes = json.load(file)
     
pprint(jokes)

app = Application(broker_adress="localhost:9092", consumer_group="text_splitter")

jokes_topic = app.topic(name= "jokes", value_serializer="json")
# print(jokes_topic)

def main():
    with app.get_producer() as producer:
        print(producer)

# den här koden körs när man exikuverar scriptet och inte när man importerar moduler
if __name__ == '__main__':
    main()