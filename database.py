#Database File for SQL Practice
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

#Commit and close the connection
conn.commit()
conn.close()

