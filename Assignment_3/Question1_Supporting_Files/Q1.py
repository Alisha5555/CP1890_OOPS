import sqlite3
import csv

def delete_old_data(cursor):
    cursor.execute("DELETE FROM Customer")

def insert_data_from_csv(cursor, csv_file):
    count = 0
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cursor.execute("INSERT INTO Customer (firstName, lastName, companyName, address, city, state, zip) VALUES (?, ?, ?, ?, ?, ?, ?)", row)
            count += 1
    return count

# Connect to the SQLite database
conn = sqlite3.connect('customers.sqlite')
cursor = conn.cursor()

# Delete old data from the Customer table
delete_old_data(cursor)

# Create Customer table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                customerID INTEGER PRIMARY KEY,
                firstName TEXT,
                lastName TEXT,
                companyName TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zip TEXT)''')

# Insert data from CSV file into Customer table
inserted_rows = insert_data_from_csv(cursor, 'customers.csv')

# Commit changes and close connection
conn.commit()
conn.close()

print("Customer Data Importer\n")
print("CSV file: customers.csv")
print("DB file: customers.sqlite")
print("Table name: Customer\n")
print("All old rows deleted from Customer table.")
print(inserted_rows, "row(s) inserted into Customer table.")