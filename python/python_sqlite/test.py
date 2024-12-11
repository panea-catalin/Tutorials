import sqlite3

# Connect to the database
conn = sqlite3.connect("sqlite.db")

# Create a cursor
cursor = conn.cursor()

# Check data in the table
cursor.execute("SELECT * FROM albums")
all_records = cursor.fetchall()
print("All records in the table:\n", all_records)

# Check records with 'The%' in title
print("\nResults from a LIKE query:\n")
sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
cursor.execute(sql)
like_results = cursor.fetchall()
print(like_results)

# Close the connection
conn.close()