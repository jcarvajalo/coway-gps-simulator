
from calendar import c
from paho.mqtt import client as mqtt_client
import os


#This class define the connection in a broker mqtt and returns the client connection
class Mqtt_connet:
    def __init__(self,broker, port, client_id, username, password):
        self.broker = broker
        self.port = port
        self.client_id = client_id
        self.username = username
        self.password = password
    
    def connect_mqtt(self,) ->  mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                 print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        
        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client


#Variable to enviroment system
MQTT_BROKER    = 
MQTT_PORT      = 1883
MQTT_CLIENT_ID = os.getenv('MQTT_CLIENT_ID')
MQTT_USER      = os.getenv('MQTT_USER')
MQTT_PASSWORD  = os.getenv('MQTT_PASSWORD')



mqtt_broker = Mqtt_connet(MQTT_BROKER,MQTT_PORT,MQTT_CLIENT_ID,MQTT_USER,MQTT_PASSWORD)
client = mqtt_broker.connect_mqtt()
print(client)