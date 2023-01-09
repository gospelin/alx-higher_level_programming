#!/usr/bin/python3
"""Query to select all rows from states table."""
import MySQLdb
from sys import argv

db_key = []

for args in argv[1:]:
    db_key.append(args)

conn = MySQLdb.connect(
                        host="localhost",
                        port=3306, user=f"{db_key[0]}",
                        passwd=f"{db_key[1]}",
                        db=f"{db_key[2]}"
                      )
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")

query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()
conn.close()
