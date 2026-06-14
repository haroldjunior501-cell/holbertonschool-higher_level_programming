#!/usr/bin/python3
"""Lists states matching a name argument, safe from MySQL injection."""
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
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
