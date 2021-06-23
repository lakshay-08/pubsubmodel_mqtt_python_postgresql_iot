import paho.mqtt.subscribe as subscribe
from datetime import datetime
import uuid
import psycopg2


def add_data_to_db(topic, payload):
    """
    :param topic: subscribed topic
    :param payload: cleaned payload from sensor
    :return:
    """
    # Get the current time
    now = datetime.now()
    # Format the current time
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # Generate uniqueID
    id1 = str(uuid.uuid1())
    # Connect to the database
    conn = psycopg2.connect(
        database="mydb", user='postgres', password='password', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO SENSORDATA(ID, DATE_TIME, TOPIC, PAYLOAD) 
    VALUES (%s, %s, %s, %s)''', (id1, dt_string, topic, payload))
    conn.commit()
    # Closing the connection
    conn.close()


def on_message_print_add_to_db(client, userdata, message):
    """
    :param client: client information
    :param userdata: contains userdata
    :param message: contains topic and payload sent
    """
    payload_cleaned = str(message.payload)
    payload_cleaned = payload_cleaned.replace('\'', '').replace('b', '')
    add_data_to_db(message.topic, payload_cleaned)
    print("%s %s" % (message.topic, message.payload))
    print("The above Records inserted........")


def create_database_and_table():
    """
    creates database only if it does not exists otherwise drops an exception and table
    """
    # subscribing to a topic from the client
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='password', host='localhost', port='5432'
    )
    conn.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # Preparing query to create a database
    sql = '''CREATE database mydb'''
    # Creating a database
    cursor.execute(sql)
    print("Database created successfully!!!")
    conn = psycopg2.connect(
        database="mydb", user='postgres', password='password', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # Doping table if already exists.
    cursor.execute("DROP TABLE IF EXISTS SENSORDATA")
    # Creating table as per requirement
    sql = '''CREATE TABLE SENSORDATA(
       ID CHAR(128) NOT NULL,
       DATE_TIME CHAR(30),
       TOPIC CHAR(40),
       PAYLOAD CHAR(50)
    )'''
    cursor.execute(sql)
    print("Table created successfully!!!")
    conn.commit()
    # Closing the connection
    conn.close()


def main():
    help(add_data_to_db)
    help(on_message_print_add_to_db)
    create_database_and_table()
    subscribe.callback(on_message_print_add_to_db, "sensor/test/room_temp", hostname="localhost")


if __name__ == "__main__":
    main()
