#!/usr/bin/python3
import MySQLdb
import sys
"""Module to query a table for all rows"""

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

query = ("SELECT cities.name FROM cities \
        INNER JOIN states ON states.id=cities.state_id AND \
        states.name=%s ORDER BY cities.id")

state = sys.argv[4]
cur.execute(query, (state,))

rows = cur.fetchall()
count = 0
for row in rows:
    size = len(row)
    for col in range(0, len(row)):
        print("{}".format(row[col]), end="")
        if col <= size - 1 and count < len(rows) - 1:
            print(", ", end="")
    count += 1
print("")
cur.close()
if (__name__ == "__main__"):
    pass
