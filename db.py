import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('questions.db')

# Create a cursor object
cursor = conn.cursor()

# Function to display table data
def display_table_data(table_name, header, query):
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print(f"\nContents of {table_name} Table")
        print(header)
        print("-" * len(header))
        for row in rows:
            print(row)
    else:
        print(f"No data available in {table_name} table.")

# Query to display data from the user table
display_table_data(
    "user",
    f"{'ID':<5} {'Name':<20} {'Password':<20} {'Expert':<10} {'Admin':<10}",
    "SELECT * FROM user;"
)

# Query to display data from the questions table
display_table_data(
    "questions",
    f"{'ID':<5} {'Question Text':<40} {'Answer Text':<40} {'Asked By ID':<15} {'Expert ID':<10}",
    "SELECT * FROM questions;"
)

# Close the connection
conn.close()
