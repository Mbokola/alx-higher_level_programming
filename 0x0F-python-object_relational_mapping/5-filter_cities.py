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
    query = 'SELECT cities.name FROM cities INNER JOIN states ON \
cities.state_id = states.id WHERE states.name = %s'
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
