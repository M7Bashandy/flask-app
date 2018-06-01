import psycopg2

conn = psycopg2.connect(database="nodes", user="root", password="root", host="127.0.0.1", port="5432")
print "Opened DVD Rental Database Successfully"

cur = conn.cursor()
cur.execute("""CREATE TABLE node (
          id SERIAL PRIMARY KEY,
          parent_id INTEGER REFERENCES info(id),
          node_name VARCHAR (20)
          )""")
print "Table created..."

conn.commit()
conn.close()