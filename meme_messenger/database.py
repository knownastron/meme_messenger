import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect("phone_numbers.db") # connects to database
    cur = conn.cursor() # creates cursor object
    cur.execute("""CREATE TABLE IF NOT EXISTS phone_numbers (country VARCHAR,
                                                        area VARCHAR,
                                                        phone_number VARCHAR,
                                                        sub_date DATETIME,
                                                        UNIQUE (country, area, phone_number))""")
    conn.commit()
    return conn

def get_database():
    conn = sqlite3.connect("db.sqlite3")
    return conn

def insert(conn, country, area, phone_number):
    cur = conn.cursor()
    time = str(datetime.now())
    cur.execute("INSERT OR REPLACE INTO phone_numbers VALUES (?,?,?, ?)", (country, area, phone_number, time))
    conn.commit()

def print_table(conn, table):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(table)) # * means all
    rows = cur.fetchall()
    print(rows)

def get_table(conn, table):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(table)) # * means all
    rows = cur.fetchall()
    return rows

def delete_number(conn, country, area, phone_number):
    cur = conn.cursor()

def date_selector(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phone_numbers WHERE sub_date < '2019-02-02 15:15:23.091300'")
    rows = cur.fetchall()
    print(rows)

def main():
    conn = get_database()
    print_table(conn, PhoneNumber)

if __name__ == "__main__":
    main()
