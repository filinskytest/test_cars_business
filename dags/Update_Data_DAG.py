import psycopg2
from psycopg2 import sql
import datetime as dt
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from CLIENT_insert_db import insert_db
import CLIENT_generate_random as CLIENT_generate_random
import CAR_generate_random as CAR_generate_random
import CAR_generate_random
import CAR_insert_db
import RENTBOOK_insert_db

args = {
    'owner': 'airflow', 
    'start_date': dt.datetime(2024, 6, 4),  
    'retries': 1, 
    'retry_delay': 0,  
}

dag = DAG(
    dag_id='Update_Data_DAG',
    schedule_interval=None,
    default_args=args,
)

# Check connect to DB
def connect_db():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky'
    )
    cur = conn.cursor()
    cur.close()
    conn.close()

# Drop table RentBook
def drop_table_rentbook():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky'
    )
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS RentBook;")

    conn.commit()

    cur.close()
    conn.close()

# Drop table Client
def drop_table_client():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky'
    )
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Client;")

    conn.commit()

    cur.close()
    conn.close()

# Drop Table Car
def drop_table_car():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky'
    )
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Car;")

    conn.commit()

    cur.close()
    conn.close()

# Create table Client and fill data
def insert_to_client():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky'
    )
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE Client
                (
                ID SERIAL PRIMARY KEY,
                First_Name VARCHAR(50) NOT NULL,
                Second_Name VARCHAR(50) NOT NULL,
                Third_Name VARCHAR(50) NOT NULL,
                Serial_Passport int NOT NULL,
                Number_Passport int NOT NULL,
                Passport VARCHAR(50) GENERATED ALWAYS AS (Serial_Passport || ' ' || Number_Passport) STORED,
                Country VARCHAR(50) NOT NULL
                );""")

    conn.commit()

    cur.close()
    conn.close()

    client_data = CLIENT_generate_random.generate_random_fio(25)
    insert_db(client_data)

# Create table Car and fill data
def insert_to_car():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky'
    )
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE Car
                (
                ID SERIAL PRIMARY KEY,
                Brand VARCHAR(50) NOT NULL,
                RentPrice numeric(18,2) NOT NULL
                );""")

    conn.commit()

    cur.close()
    conn.close()

    car_data = CAR_generate_random.price
    CAR_insert_db.insert_db(car_data)

# Create table RentBook and fill data
def insert_to_rentbook():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        dbname='cars',
        user='filinsky',
        password='filinsky',
        client_encoding='utf8'
    )
    cur = conn.cursor()
    
    cur.execute("""
                CREATE TABLE RentBook
                (
                ID SERIAL PRIMARY KEY,
                Date DATE NOT NULL,
                Time INT NOT NULL,
                Pre_Paid BOOLEAN NOT NULL,
                CarID INT NOT NULL,
                ClientID INT NOT NULL,
                FOREIGN KEY (CarID) REFERENCES Car (ID),
                FOREIGN KEY (ClientID) REFERENCES Client (ID)
                );""")
    conn.commit()

    RENTBOOK_insert_db.insert_rentbook_data(conn)
    conn.close()

start = BashOperator(
    task_id='start',
    bash_command='echo "Here we start! "',
    dag=dag,
)
# Connect_to_DB
Connect_to_DB = PythonOperator(
    task_id='connect_db',
    python_callable=connect_db,
    dag=dag,
)
# Drop_Table_RentBook
Drop_Table_RentBook = PythonOperator(
    task_id='drop_table_rentbook',
    python_callable=drop_table_rentbook,
    dag=dag,
)
# Drop_Table_Client
Drop_Table_Client = PythonOperator(
    task_id='drop_table_client',
    python_callable=drop_table_client,
    dag=dag,
)
# Drop_Table_Car
Drop_Table_Car = PythonOperator(
    task_id='drop_table_car',
    python_callable=drop_table_car,
    dag=dag,
)

# Create_Table_Client_Fill
Create_Table_Client_Fill = PythonOperator(
    task_id='insert_to_client',
    python_callable=insert_to_client,
    dag=dag,
)

# Create_Table_Car_Fill
Create_Table_Car_Fill = PythonOperator(
    task_id='insert_to_car',
    python_callable=insert_to_car,
    dag=dag,
)

# Create_Table_RentBook_Fill
Create_Table_RentBook_Fill = PythonOperator(
    task_id='insert_to_rentbook',
    python_callable=insert_to_rentbook,
    dag=dag,
)

start >> Connect_to_DB >> Drop_Table_RentBook >> Drop_Table_Client >> Drop_Table_Car >> Create_Table_Client_Fill >> Create_Table_Car_Fill >> Create_Table_RentBook_Fill