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
    sql = """SELECT cities.id, cities.name FROM cities
          INNER JOIN states on cities.state_id = states.id
          WHERE states.name = %s
          ORDER BY cities.id"""

    # Execute sql command
    cur.execute(sql, (state,))

    # Store the output from database
    states = cur.fetchall()

    # output = set()

    # Display the result
    # for state in states:
    #    output.add(state[1])

    # for state in output:
    #    print(", ".join(state))

    print(", ".join([state[1] for state in states]))

    # Close database connection
    cur.close()
    db.close()
