import sqlite3

conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()

# update some data
sql = """
    UPDATE albums
    SET artist = 'John Doe'
    WHERE artist = 'Andy Hunter'
"""

cursor.execute(sql)
conn.commit()