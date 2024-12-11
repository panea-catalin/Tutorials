import sqlite3

conn = sqlite3.connect("sqlite.db")

cursor = conn.cursor()

sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("Red")])
print(cursor.fetchall())

print("\nHere's a list of all the records in the table:\n")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

print("\nResults from a LIKE query:\n")
sql = """
SELECT * FROM albums
WHERE title LIKE 'The%'"""
cursor.execute(sql)
print(cursor.fetchall())