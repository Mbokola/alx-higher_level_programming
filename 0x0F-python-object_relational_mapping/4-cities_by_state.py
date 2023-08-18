#!/usr/bin/python3
"""
    lists all states from the database hbtn_0e_0_usa
    parameterized to avoid sql injection
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'

    db = MySQLdb.connect(host=host, user=mysql_username, passwd=mysql_password,
                         db=database_name, port=3306)

    cursor = db.cursor()
    query = 'SELECT cities.id, cities.name, states.name FROM cities, states\
 WHERE states.id = cities.state_id ORDER BY cities.id ASC'
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
