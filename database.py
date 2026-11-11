
import sqlite3
#Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

#Create a sample table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        price INTEGER NOT NULL,
        mileage INTEGER NOT NULL)
        ''')

    

#Insertt a list of 20 cars
cursor.execute('''
INSERT INTO vehicles (id, make, model, year, price, mileage)
VALUES
    (1, 'Toyota', 'Camry', 2022, 22500, 35000),
    (2, 'Honda', 'Civic', 2021, 19500, 42000),
    (3, 'BMW', '330i', 2020, 27000, 51000),
    (4, 'Kia', 'Stinger', 2022, 32000, 28000),
    (5, 'Subaru', 'WRX', 2023, 29500, 19000),
    (6, 'Toyota', 'Corolla', 2020, 17500, 58000),
    (7, 'Honda', 'Accord', 2022, 26000, 31000),
    (8, 'BMW', '540i', 2019, 28500, 67000),
    (9, 'Lexus', 'IS 350', 2021, 34500, 39000),
    (10, 'Nissan', 'Altima', 2020, 18500, 61000),
    (11, 'Hyundai', 'Elantra', 2023, 22000, 17000),
    (12, 'Mazda', 'Mazda3', 2021, 21500, 44000),
    (13, 'Audi', 'A4', 2020, 25500, 53000),
    (14, 'Mercedes-Benz', 'C300', 2021, 31000, 42000),
    (15, 'Genesis', 'G70', 2022, 33500, 29000),
    (16, 'Acura', 'TLX', 2021, 29500, 38000),
    (17, 'Volkswagen', 'Jetta', 2019, 16000, 72000),
    (18, 'Ford', 'Mustang', 2022, 30500, 26000),
    (19, 'Chevrolet', 'Camaro', 2020, 28000, 48000),
    (20, 'Subaru', 'BRZ', 2023, 31500, 15000);
    ''')

#Commit and close the connection
conn.commit()
conn.close()