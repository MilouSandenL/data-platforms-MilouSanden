# consumer tar emot meddelanden från kafka, bearbetar och skriver ut på ett läsbart sätt.
from quixstreams import Application

# Skapar en consumer som prenumererar på kafka-brokern och den specifika consumer group (som vi har i producern) för att vara i samma grupp och kunna hantera meddelanden som produceras.
# aouto_offset_reset='earliest' används för att om consumern startar om- kommer den börja läsa från det första meddelandet i topicen.
app = Application(broker_address="localhost:9092", consumer_group="order_group", auto_offset_reset="earliest")

# skapar topic där man får alla meddelanden från producern. Gör om (deseralizerar) meddelandet från json till python-objekt.
orders_topic = app.topic(name="orders_topic", value_deserializer="json")

# skapar en dataframe som tar emot alla meddelanden från topicen order_topic. dataframe --> varje rad är ett meddelande.
sdf = app.dataframe(topic=orders_topic)

# Funktion för att bearbeta varje ordermeddelande. skriver ut information om ordern.
def process_order(order):
    print(f"\nInput: {order}")
    print(f"Order ID: {order['order_id']}")
    print(f"Kund: {order['customer']}")

    total_price = 0
    for product in order["products"]:
        product_name = product["name"]
        price = product["price"]
        quantity = product["quantity"]
        total_price += price * quantity
        print(f"Produkt: {product_name:<20} Antal: {quantity:<5} Pris: {price:.2f}")

    print(f"Total pris: {total_price:.2f}")

# varje gång ett nytt meddelande (order) kommer in från kafka, så bearbetas den med funktionen process_order.
sdf.update(lambda message: process_order(message))

# Starta applikationen
if __name__ == '__main__':
    print("Startar Kafka consumer...")
# app.run() används så att applikationen ska startas, vilket innebär att kafka consumer börjar prenumerera på topicen och bearbetar inkommande meddelanden.
    app.run()
