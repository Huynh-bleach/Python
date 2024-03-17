import random
import time

from paho.mqtt import client as mqtt_client


broker = 'ngoinhaiot.com'
port = 1111
topic = "Huynh1611/python"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'Huynh1611'
password = 'D4D94FE836AB48D8'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    while True:
        value = input("Nhap 0(OFF led) hoac 1(ON LED) hoac THOAT: ")
       # msg = f"messages: {msg_count}"
        if value == "THOAT":
            break
        msg='{"kind":3,"val":'+value+'}'
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        
        


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
