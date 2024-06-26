#!/usr/bin/python3
"""
A Python script that lists all states from the database hbtn_0e_0_usa
The script take 3 arguments: mysql username, mysql password and database
name (no argument validation needed)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connecting to the database and listing all the states in hbtn_0e_0_usa
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    myDB = MySQLdb.connect(
            host="localhost",
            user=username,
            port=3306,
            passwd=password,
            db=database
            )

    # Executing statement
    cursor = myDB.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Returning results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Closing the cursor and the database connection
    cursor.close()
    myDB.close()


"""
# Import statements
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Accessing user credentials from the command line
user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Database URL
db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
# Base = declarative_base()

# Creating the engine
engine = create_engine(db_url.format(user, password, database))

# Session
Session = sessionmaker(bind=engine)
session = Session()

# Querying the results
results = session.query().all()
print(results)
"""
