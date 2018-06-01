#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","nodes" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS info")

# Create table as per requirement
sql = """CREATE TABLE info (
         id  INT NOT NULL AUTO_INCREMENT,
         node_name  CHAR(20) NOT NULL,
         parent_id INT,
         PRIMARY KEY (id),
         FOREIGN KEY (parent_id) REFERENCES info (id)
          )"""

cursor.execute(sql)

# disconnect from server
db.close()