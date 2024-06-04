import psycopg2
import CLIENT_generate_random as CLIENT_generate_random


fio_pass = CLIENT_generate_random.generate_random_fio(25)


def insert_db(fio_pass):
    try:
        conn = psycopg2.connect(
            host='db',
            port='5432',
            dbname='cars',
            user='filinsky',
            password='filinsky'
        )
        cur = conn.cursor()
        print('Connected')
        
        insert_query = """
            INSERT INTO Client (First_Name, Second_Name, Third_Name, Country, Serial_Passport, Number_Passport)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        for fio in fio_pass:
            cur.execute(insert_query, fio)
        
        conn.commit()
        print("Inserted")
    except Exception as e:
        conn.rollback
        print("Failed:", e)
    finally:
        cur.close()
        conn.close()