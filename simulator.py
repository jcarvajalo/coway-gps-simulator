from  mqtt_connection import client
import os 
import time

#Enviorement varibales
COW_DATA_GPS =  os.getenv("PATH_DATA_COWAY") #This variable get a txt file to contain the coordinates of cow 
COW_TOPIC =  os.getenv("COW_TOPIC")  
COW_NAME =  os.getenv("COW_NAME")
COW_REGISTER_ID = os.getenv("COW_REGISTER_ID")
COW_COLOR = os.getenv("COW_COLOR")

def build_the_payload(coordinates,reisterId, name, cowColor):
    payload = "{cowLocation:"+str(coordinates)+",registerId:'"+str(reisterId)+"',name:'"+str(name)+"',cowColor:"+str(cowColor)+"}"
    return payload
    

while True:
    cow = open(COW_DATA_GPS,"r")
    for i in cow:
        payload = build_the_payload(i,COW_REGISTER_ID, COW_NAME, COW_COLOR)
        time.sleep(2)
        response = client.publish(COW_TOPIC, payload)
        print(payload)