import mysql.connector

# Establish the connection
con_obj = mysql.connector.connect(
    user='root',
    password='root',
    host='127.0.0.1'
)

# Check if the connection was successful
if con_obj.is_connected():
    print("Connection established successfully!")

    # Create a cursor object
    cur_obj = con_obj.cursor()

    # Execute the SQL query to create the database (fixed typo)
    try:
        cur_obj.execute('CREATE DATABASE student')
        print("Database created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    # Close the cursor and connection
    cur_obj.close()
else:
    print("Failed to connect to MySQL.")
    
# Close the connection
con_obj.close()
