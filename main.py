import serial
import time
import paho.mqtt.client as mqtt #need to install  pip install paho-mqtt==1.6.0


client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')


ser=serial.Serial('COM3',115200,timeout=0.5)


while True:
    data=ser.readline()
    data=data.decode('utf-8')
    try:
        data=int(data)
        print(data)
        client.publish('revanth/data',str(data))
        print('Data published')
    except:
        pass
#print(data)