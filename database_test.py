import json
import sqlite3

# Load the data from the JSON file
with open('user_data.json', 'r') as f:
    data = json.load(f)

# Create a new SQLite database and establish a connection
conn = sqlite3.connect(r'D:\Ver_5_updated-main\database\\user_data.db')
c = conn.cursor()

# Create a new table if it doesn't already exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT,
        phone1 TEXT,
        phone2 TEXT,
        phone3 TEXT
    )
''')

# Insert the data into the table
def insert_user(user_id, name, contact1, contact2, contact3):
    # Connect to the database
    
    conn = sqlite3.connect(r'D:\Ver_5_updated-main\database\\user_data.db')
    c = conn.cursor()

    # Insert the user's details into the users table
    c.execute('''
        INSERT OR IGNORE INTO users (id, name, phone1, phone2, phone3)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, name, contact1, contact2, contact3))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
# Fetch all the rows

def update_user(user_id, name, contact1, contact2, contact3):
    # Connect to the database
    conn = sqlite3.connect(r'D:\Ver_5_updated-main\database\\user_data.db')
    c = conn.cursor()

    # Update the user's details in the users table
    c.execute('''
        UPDATE users
        SET name = ?, phone1 = ?, phone2 = ?, phone3 = ?
        WHERE id = ?
    ''', (name, contact1, contact2, contact3, user_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def delete_user(user_id):
    # Connect to the database
    conn = sqlite3.connect(r'D:\Ver_5_updated-main\database\\user_data.db')
    c = conn.cursor()

    # Delete the user from the users table
    c.execute('''
        DELETE FROM users
        WHERE id = ?
    ''', (user_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
def print_database():
    # Connect to the database
    conn = sqlite3.connect(r'D:\Ver_5_updated-main\database\\user_data.db')
    c = conn.cursor()

    # Select all data from the users table
    c.execute("SELECT * FROM users")

    # Fetch all the rows
    rows = c.fetchall()

    for row in rows:
        print(row)

    # Close the connection
    conn.close()

#print_database()