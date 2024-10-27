import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')

# Create a cursor object
cursor = conn.cursor()

# Read the SQL file
with open('schema.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("SQL script executed successfully.")
