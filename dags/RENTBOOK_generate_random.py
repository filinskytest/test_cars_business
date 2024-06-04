import random
from datetime import timedelta, date
import CAR_generate_random
import CLIENT_generate_random

date_start = date(2023, 6, 3)
date_end = date(2024, 6, 3)

dates = [date_start + timedelta(days=random.randint(0, (date_end - date_start).days)) for _ in range(10000)]
dates_random = tuple(dates)


#############################################_________GENERATE_TIME_RENT_________#############################################
time_rent = list(range(1, 24))  # Диапазон от 1 до 23 включительно
random_time_rent = random.choices(time_rent, k=10000)
random_time_rent_tuple = tuple(random_time_rent)


#############################################_________GENERATE_PAID_________#############################################
paid = [random.choice([True, False]) for _ in range(10000)]
random_paid = tuple(paid)

 #############################################_________GENERATE_CARID_________#############################################
car_list = CAR_generate_random.car_list
CarID = random.choices(range(1, len(car_list) + 1), k=10000)

#############################################_________GENERATE_CLIENTID_________#############################################
second_names = CLIENT_generate_random.second_names
clientid = random.choices(range(1, len(second_names) + 1), k=10000)
