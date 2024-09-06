# the psycopg2 can be import to create connection to the database
import psycopg2

class wrapper:
    # function that is create for the connection to the database
    def __init__(self, dbname, user, password, host = 'localhost', port= 5433):
        """Initialize the PostgreSQL wrapper with the given database connection parameters."""
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None
    # function that establish a connection   
    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connection to the database established successfully.")
        except OperationalError as e:
            print(f"An error occurred while connecting to the database: {e}")
            self.connection = None
            self.cursor = None
    # Create function that create table in the database
    # name of table is student and create if its not already exist
    # and then commit it
    def create(self):
        try:
            self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Student (
            id SERIAL PRIMARY KEY,
            student_name VARCHAR(100),
            student_age INT,
            student_marks INT,
            address Varchar(255)    
        );"""
    ) 
            self.connection.commit()
            print("Table created successfully.")
        except Exception as e:
            print("table already created",e)
    # now that is insert function
    def insert(self):
        self.cursor.execute(
            """ INSERT INTO Student (student_name,student_age,student_marks,address)
            VALUES ('shanzy',20,1092,'vehari'),
                   ('saira',21,800,'mailsi'),
                   ('ayesha',30,1060,'lahore'),
                   ('saima',40,600,'burawala'),
                   ('alina',33,880,'gujrawala'),
                   ('maham',22,910,'vehari'),
                   ('ali',33,900,'lahore'),
                   ('umer',22,1000,'lahore'),
                   ('abiha',33,1030,'karachi'),
                   ('laiba',32,1080,'vehari');"""
        )
        self.connection.commit()
        print("Data insert successfully.")
        
    # update whole function in which the user can change the whole data 
    # data can be update on the base of address
    def update_whole(self,student_name,student_age,student_marks,address):
        new_address=input("enter the new address:")
        try:
            self.cursor.execute('''UPDATE Student SET student_name=%s,student_age=%s,student_marks=%s,address=%s 
                                WHERE address=%s''',(student_name,student_age,student_marks,address,new_address) 
                                )
            self.conn.commit()
            print("updated successfully")
        except Exception as e:
                print(f"An error occurred while updating the table: {e}")
        
   # update the student table.....
    def update(self):
            try:
                self.cursor.execute(" UPDATE Student SET student_age= 20 WHERE address='vehari'")
                self.connection.commit()
            except Exception as e:
                print(f"An error occurred while updating the table: {e}")
    # Drop the student table from database
    def drop(self):
            try:
                self.cursor.execute("DROP TABLE IF EXISTS Student;")
                self.connection.commit()
                print("Table dropped successfully.")
            except Exception as e:
                print(f"An error occurred while dropping the table: {e}")
                
    def disconnect(self):
        """Close the cursor and connection."""
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        print("Disconnected from the database.")
                
db=wrapper("postgres","postgres",123)
while True:
        print("ENTER YOUR CHOICE:")
        print("2 - Create")
        print("3 - Insert")
        print("4 - Update_whole")
        print("5 - Update")
        print("6 - Drop")
        print("7 - Disconnect")
        print("8 - EXIST")
        
        choice = input("Enter your choice: ")

        if choice == '8':
            print("Exit")
            break

        if choice in ['1', '2', '3', '4', '5','6','7']:
            if choice == '1':
                db.connect()
            elif choice == '2':
                db.create()
            elif choice == '3':
                db.insert()
            elif choice == '4':
                name=input("enter the new_name:")
                age=int(input("enter the new_age:"))
                marks=int(input("enter the new_marks:"))
                address=input("enter the  new_address:")
                db.update_whole(name,age,marks,address)
            elif choice == '5':
                db.update()
            elif choice=='6':
                db.drop()
            elif choice=='7':
                db.disconnect()
        else:
            print("Invalid Input")
    

