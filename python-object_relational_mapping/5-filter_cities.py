#!/usr/bin/python3
"""Lists all cities of a given state from the database `hbtn_0e_4_usa`."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Exit if incorrect number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py mysql_username mysql_password database_name state_name")
        sys.exit(1)

    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:5]

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

        # Query to select cities of the given state, sorted by city ID
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        # Execute query with state name parameter
        cur.execute(query, (state_name,))

        # Fetch results and print cities as a comma-separated string
        cities = cur.fetchall()
        if cities:
            print(", ".join([city[0] for city in cities]))
        else:
            print("")

    except MySQLdb.MySQLError as e:
        # Handle database errors
        print(f"Error: {e}")

    finally:
        # Close cursor and database connection
        if db:
            cur.close()
            db.close()
