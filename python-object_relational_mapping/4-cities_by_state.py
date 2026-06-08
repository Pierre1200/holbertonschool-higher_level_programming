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

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    states = cursor.fetchall()
    for row in states:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    cursor.close()
    db.close()
