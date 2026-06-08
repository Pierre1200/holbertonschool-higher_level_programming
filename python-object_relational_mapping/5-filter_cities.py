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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    town_list = []
    for row in states:
        town_list.append(row[0])
    print(", ".join(town_list))
    cursor.close()
    db.close()
