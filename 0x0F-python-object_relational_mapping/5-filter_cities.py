#!/usr/bin/python3
"""
List all cities by states from database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db = argv[3]
    state = argv[4]

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
    sql = """SELECT cities.name FROM cities
          INNER JOIN states on cities.state_id = states.id
          WHERE states.name = %s
          ORDER BY cities.id"""

    # Execute sql command
    cur.execute(sql, (state,))

    # Store the output from database
    states = cur.fetchall()

    output = ""

    # Concatenate the result
    for state in states:
        output += f"{state[0]}, "

    # Display states
    print(output[:-2])

    # Close database connection
    cur.close()
    db.close()
