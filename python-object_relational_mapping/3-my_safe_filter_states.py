#!/usr/bin/python3
"""
Ce module liste tous les états de la base de données hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))
    states = cursor.fetchall()
    for row in states:
        print("({}, '{}')".format(row[0], row[1]))
    cursor.close()
    db.close()
