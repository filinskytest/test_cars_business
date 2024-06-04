import psycopg2
import CAR_generate_random


car_insert = CAR_generate_random.price

def insert_db(car_insert):
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
            INSERT INTO Car (Brand, RentPrice)
            VALUES (%s, %s);
        """
        for car in car_insert:
            cur.execute(insert_query, (car, car_insert[car]))
        
        conn.commit()
        print("Inserted")
    except Exception as e:
        if conn:
            conn.rollback()
        print("Failed:", e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()