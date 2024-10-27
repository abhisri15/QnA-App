import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('questions.db')

# Create a cursor object
cursor = conn.cursor()

# Update admin status for the user with id=1
cursor.execute("UPDATE user SET admin = '1' WHERE id = 1")

# Commit the changes
conn.commit()

# Check if the update was successful
cursor.execute("SELECT * FROM user WHERE id = 1")
print("Updated record:", cursor.fetchone())

# Close the connection
conn.close()
