#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")

    cur = conn.cursor()
    cur.execute(
            "SELECT cities.name From cities "
            "join states on cities.state_id = states.id "
            "where states.name = %s"
            "ORDER BY cities.id ASC", (argv[4], ))
    query_rows = cur.fetchall()
    print(", ".join(map(lambda item: item[0], query_rows)))
    cur.close()
    conn.close()
