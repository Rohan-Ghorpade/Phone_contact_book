import sqlite3

def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (ID INTEGER PRIMARY KEY, Name TEXT, Cell TEXT, Email TEXT)''')
    conn.commit()
    conn.close()


def insert_data(name, cell, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (Name, Cell, Email) VALUES (?, ?, ?)", (name, cell, email))
    conn.commit()
    conn.close()


def fetch_data():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    data = c.fetchall()
    conn.close()
    return data


create_table()

# Insert 5 rows of data
insert_data("Rohan s ghorpade", "6360112301", "Rohanghorpade@gmail.com")
insert_data("Sunil", "6362753027", "Sunil@gmail.com")
insert_data("Rakesh", "8277490733", "Rakesh@gmail.com")
insert_data("Gokul", "8618220347", "Gokul@gmail.com")
insert_data("Raghavendra", "9108070437", "Raghavendra@gmail.com")

# Fetch and display all data
print("ID\tName\t\tCell#\t\t\tEmail")
print("-" * 50)
for row in fetch_data():
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
