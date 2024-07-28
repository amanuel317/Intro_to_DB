import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(
            user='your_username', 
            password='your_password',
            host='your_host'
        )
        cursor = cnx.cursor()
        
        # Create database
        db_name = 'alx_book_store'
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        cursor.execute(create_db_query)
        print(f"Database '{db_name}' created successfully!")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        # Close the cursor and connection
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    create_database()
