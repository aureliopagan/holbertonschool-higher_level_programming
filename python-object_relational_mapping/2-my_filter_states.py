#!/usr/bin/python3
"""Filters states by user input and displays matching states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments for MySQL username, password, database, and state name
    username, password, database, state_name = sys.argv[1:5]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Construct and execute the SQL query to find states matching the user input
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch all the rows from the executed query
    rows = cur.fetchall()

    # Print each row in the specified format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
