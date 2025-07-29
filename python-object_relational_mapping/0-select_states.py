#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa using MySQLdb."""
import MySQLdb
import sys

def list_states(username, password, dbname):
    """Connects to MySQL database and lists all states sorted by id."""
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    
    # Create a cursor object to execute SQL queries
    cur = db.cursor()
    
    # Execute the SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows from the executed query
    query_rows = cur.fetchall()
    
    # Print each row
    for row in query_rows:
        print(row)
    
    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    # Call the function to list states
    list_states(username, password, dbname)
