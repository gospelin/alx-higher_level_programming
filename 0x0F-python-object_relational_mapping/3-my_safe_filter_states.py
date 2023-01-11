#!/usr/bin/python3
"""
List all states that matches argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_key = []

    for args in argv[1:]:
        db_key.append(args)

    # Connect to Database
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=f"{db_key[0]}",
      passwd=f"{db_key[1]}",
      db=f"{db_key[2]}"
    )

    # Create a pointer to database
    cur = db.cursor()
    sql = """SELECT * FROM states
          WHERE name = %s
          ORDER BY states.id ASC"""

    # Execute sql command
    cur.execute(sql, (db_key[3],))

    # Store the output from database
    states = cur.fetchall()

    # Display the result
    for state in states:
        print(state)

    # Close database connection
    cur.close()
    db.close()
