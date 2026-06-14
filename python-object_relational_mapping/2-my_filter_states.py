#!/usr/bin/python3
"""Lists states matching a name given as argument using string format."""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
