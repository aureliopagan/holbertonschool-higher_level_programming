#!/usr/bin/python3
"""Lists all states with a name starting with N (uppercase) from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


def main():
    """Main function to filter and display states starting with 'N'."""
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    # Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8"
    )
    
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()
    
    # Execute the SQL query to select states starting with 'N' and order by id
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    # Fetch all the rows from the executed query
    query_rows = cur.fetchall()
    
    # Print each row in the specified format
    for row in query_rows:
        print(row)
    
    # Close the cursor and database connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
