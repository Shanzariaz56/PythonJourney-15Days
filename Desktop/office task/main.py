import psycopg2

connection = psycopg2.connect(host="localhost",
                      dbname="postgres",
                      user="postgres",
                      password="123",
                      port=5433)
cur = connection.cursor() 
# create table in database
cur.execute("""
        CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    """) 
# insert data in table
cur.execute(""" INSERT INTO person(name,age)
            VALUES   ('JohnDoe', 30),
        ('JaneSmith', 25),
        ('AliceJohnson', 35),
        ('BobBrown', 40);
            """)
""" def drop(self):
            try:
                self.cursor.execute("DROP TABLE IF EXISTS Student;")
                self.connection.commit()
                print("Table dropped successfully.")
            except Exception as e:
                print(f"An error occurred while dropping the table: {e}")"""

# excute any condition...
# select a single data
cur.execute(""" SELECT * FROM person where name='JohnDoe'""")
print(cur.fetchone())

# select more than one rows
cur.execute(""" SELECT * FROM person where age >30;""")
for i in cur.fetchall():
    print(i)
    
#cur.mogrify("""SELECT * FROM person WHERE starts_with(name,%j) """)
connection.commit()
cur.close()
connection.close()

