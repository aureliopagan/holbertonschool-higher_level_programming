#!/usr/bin/python3
"""Lists all cities from the database `hbtn_0e_4_usa` sorted by cities.id."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Exit if incorrect number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py mysql_username mysql_password database_name")
        sys.exit(1)

    # Get command-line arguments
    username, password, database = sys.argv[1:4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create cursor to execute queries
        cur = db.cursor()

        # Query to select cities and their states, sorted by city ID
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """

        # Execute query and fetch results
        cur.execute(query)
        rows = cur.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.MySQLError as e:
        # Handle database errors
        print(f"Error: {e}")

    finally:
        # Close cursor and database connection
        if db:
            cur.close()
            db.close()
