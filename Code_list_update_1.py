import psycopg2


class Add_code():
    """Insert a new website login parameters into the DB"""

    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def database_export (self):
        """Connection to the Database Login"""

        ##DB choice
        #database_choice = input("In which databse would you like to add datas ? ")
        #print("Insertion of the datas into the database {}".format(database_choice))
        
        print("Insertion of the datas into the usernames table and the passwords table.")
        
        #Statements
        psql_username = (
            """INSERT INTO usernames (websites, usernames)
                VALUES (%s, %s) RETURNING id;
            """
        )

        psql_password = (
            """INSERT INTO passwords (websites, passwords)
                VALUES (%s, %s) RETURNING id;
            """
        )

        connection = None
        id = None

        try:
            print("Connection to the database server...")
            #Connection to the databse
            connection = psycopg2.connect(
                database = "login",
                user = "postgres",
                password = "SA1W4ntU",
                host = "localhost",
                port = "5432",
            )

            print("Connection to the database server established")
            cursor = connection.cursor()

            #Execution of the statement
            cursor.execute(psql_username, (self.website, self.username))
            cursor.execute(psql_password, (self.website, self.password))

            #Save modifications
            print("Changes saved")
            connection.commit()

            #Close the cursor
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("We meet a problem during the connection so we choose to end it...", error)
        finally:
            if connection is not None:
                connection.close()
                print("Connection closed.")
                
        return id
    
    def login_export(self):
            print("You correctly exported your login passwords {} and {} from the website {} into the database.".format(self.username, self.password, self.website)) 

insertion = True
while insertion:
    website = input("What is the website you created a new account in  ? ")
    usernames = input(" what is the username you used ? ")
    passwords = input("what is the password you entered ? ")
    new_login = Add_code(website, usernames, passwords)
    new_login.database_export()
    new_login.login_export()