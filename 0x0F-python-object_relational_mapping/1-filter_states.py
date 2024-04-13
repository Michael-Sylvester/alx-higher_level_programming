#!/usr/bin/python3
import MySQLdb
import sys
"""Module to query a table for all rows"""

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

rows = cur.fetchall()
for row in rows:
    print("{}".format(row))
cur.close()
if (__name__ == "__main__"):
    pass
