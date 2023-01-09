#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

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

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
