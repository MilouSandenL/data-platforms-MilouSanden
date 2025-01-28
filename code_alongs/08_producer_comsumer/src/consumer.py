# quixstrems är till för att arbeta mot kafka - en högre nivå (längre bort från ursprungskällan, man har tagit bort komplicerat språk)
from quixstreams import Application

app = Application(broker_address="localhost:9092", consumer_group="text-splitter", auto_offset_reset="earliest")

# behöver läsa in det i json igen, så vi ska deserialize it.
jokes_topic = app.topic(name="jokes", value_deserializer="json")

# skapar en dataframe, en quixstreams dataframe. lazy evaluation, så att för mycket data inte strömmar i onödan.
# skapar en dataframe av topic
sdf = app.dataframe(topic=jokes_topic)

# def print_message(message):
    #print(message)
# sdf.update(print_message)

# (en anonym funktion) en lambda funktion - motsvarar dom tre raderna över
sdf.update(lambda message: print(f"input message: {message}"))

# transformations - apply lägger man till en funktion för att transformera.
# vill splitta på orden

def split_word(message):
    return [{"word": word} for word in message["joke_text"].split()]

sdf = sdf.apply(split_word, expand=True)

sdf["length"] = sdf["word"].apply(lambda word: len(word))

sdf.update(lambda row: print (f"Output: {row}"))


# kört inte fören vi kör: app.run()
if __name__ == '__main__':
    app.run()