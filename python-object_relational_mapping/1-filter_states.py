#!/usr/bin/python3
"""Lists states whose name starts with N from the database hbtn_0e_0_usa."""
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
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
