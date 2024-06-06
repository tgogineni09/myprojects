import mysql.connector
from mysql.connector import Error

try:
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        passwd="123456",  # Replace with your MySQL password
        database="db1"
    )

    if dataBase.is_connected():
        print("Successfully connected to the database")
        cursorObject = dataBase.cursor()

        # Correct multi-line SQL query
        query = """
        SELECT o.orderNumber, o.orderDate, o.status, c.customerName
	FROM orders o
	JOIN customers c ON o.customerNumber = c.customerNumber
	WHERE o.shippedDate IS NULL;


        """

        cursorObject.execute(query)
        myresult = cursorObject.fetchall()

        for x in myresult:
            print(x)

except Error as e:
    print(f"Error: {e}")

finally:
    if dataBase.is_connected():
        dataBase.close()
        print("MySQL connection is closed")
