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

    # Construct a parameterized SQL query to find states matching the user input
    # Using parameterized queries prevents SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    rows = cur.fetchall()

    # Print each row if there are results
    if rows:
        for row in rows:
            print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
