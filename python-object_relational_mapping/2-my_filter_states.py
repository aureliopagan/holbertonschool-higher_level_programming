#!/usr/bin/python3
"""Filters states by user input and displays matching states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


def main():
    """Main function to filter and display states matching the user input."""
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the query to find states matching the user input
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


if __name__ == "__main__":
    main()
