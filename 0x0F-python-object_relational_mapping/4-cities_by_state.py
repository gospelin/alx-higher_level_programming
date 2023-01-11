#!/usr/bin/python3
"""
List all cities in states from database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db = argv[3]

    # Connect to Database
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=user,
      passwd=password,
      db=db
    )

    # Create a pointer to database
    cur = db.cursor()
    sql = """SELECT cities.id, cities.name, states.name FROM cities
          INNER JOIN states ON cities.state_id = states.id
          ORDER BY cities.id ASC"""

    # Execute sql command
    cur.execute(sql)

    # Store the output from database
    states = cur.fetchall()

    # Display the result
    for state in states:
        print(state)

    # Close database connection
    cur.close()
    db.close()
