from psycopg2 import sql
import psycopg2
import RENTBOOK_generate_random

def insert_rentbook_data(conn):
    insert_dates = RENTBOOK_generate_random.dates_random
    insert_time_rent = RENTBOOK_generate_random.random_time_rent
    insert_paid = RENTBOOK_generate_random.random_paid
    insert_CarID = RENTBOOK_generate_random.CarID
    insert_clientid = RENTBOOK_generate_random.clientid

    cur = conn.cursor()
    try:
        for i in range(10000):
            cur.execute(sql.SQL("""
                INSERT INTO RentBook (Date, Time, Pre_Paid, CarID, ClientID) 
                VALUES (%s, %s, %s, %s, %s);
            """), (insert_dates[i], insert_time_rent[i], insert_paid[i], insert_CarID[i], insert_clientid[i]))
        
        conn.commit()
        print("Inserted")
    except Exception as e:
        conn.rollback()
        print("Failed:", e)
    finally:
        cur.close()
