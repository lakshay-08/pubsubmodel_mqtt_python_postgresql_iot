# MQTT Publish Subscribe model and  adding data to Database

An Example of MQTT publish and subscribe Model in python and adding the data to PostgreSQL database. 
From publish file random data will be gerated for two topics and from the subscribe file subscription to a topic will be made then the data will be added to a database mydb to table wich contains unique id, time, topic and the payload.
 

## Requirements: 
1. Python 3
   1. paho-mqtt
   2. psycopg2
2. Eclipse Mosquitto
3. MQTT Explorer

## MQTT Publish Subscribe model
![MQTT-](https://user-images.githubusercontent.com/52098775/123169631-2c1a3f80-d497-11eb-860a-5bdfe39b27f7.jpg)

## Sensordata in postgreSQL table and MQTT Explorer showing topic and payload
![Screenshot (77)](https://user-images.githubusercontent.com/52098775/123167809-b0b78e80-d494-11eb-8612-e8847843e162.png)
