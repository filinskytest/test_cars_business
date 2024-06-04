import random

car_list = ["Acura","Alfa Romeo","Aston Martin","Audi","Bentley","BMW","Bugatti","Buick","Cadillac","Chevrolet","Chrysler","Citroën","Dacia",
            "Daewoo","Daihatsu","Dodge","Ferrari","Fiat","Ford","Genesis","GMC","Honda","Hyundai","Infiniti","Jaguar","Jeep","Kia",
            "Koenigsegg","Lamborghini","Lancia","Land Rover","Lexus","Lincoln","Lotus","Maserati","Mazda","McLaren",
            "Mercedes-Benz","Mini","Mitsubishi","Nissan","Pagani","Peugeot","Porsche","Ram","Renault","Rolls-Royce","Saab",
            "Subaru","Suzuki","Tesla","Toyota","Volkswagen","Volvo"]


price = {car: round(random.uniform(100000.0, 999999.99), 2) for car in car_list}