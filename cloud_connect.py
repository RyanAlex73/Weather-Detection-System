import paho.mqtt.client as mqtt
# import wiotp.sdk.application
import json


device_type = "RaspberryPi"
device_id = "Device0001"
org_id = "1w95zu"

url = "{}.messaging.internetofthings.ibmcloud.com".format(org_id)
port = 8883
client_id = "d:{}:{}:{}".format(org_id, device_type, device_id)

topic_name = "iot-2/evt/sensor_data/fmt/json"

username = "use-token-auth"
token = "Device0001"

def on_connect(client, userdata, flags, rc):
        print("Connecting to... " + url)
        print("Connection returned result: " + mqtt.connack_string(rc))

def on_disconnect(client, userdata, rc):
        print("Disconnected from... " + url)

def on_publish(client, userdata, mid):
        print("Published a message: " + str(mid))

def on_log(client, userdata, level, buf):
        print("LOG: ", buf)

# Create the client instance
client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# debug line
client.on_log = on_log
client.username_pw_set(username=username, password=token)
client.tls_set()
client.connect(url, port, 60)

data = json.dumps({'data':"Hello World"})
while data!="quit":
    data = json.dumps({'data':data})
    (rc, mid) = client.publish(topic_name, payload=data)
    data = input()
client.disconnect()
