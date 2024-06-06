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
        print("Retrieve product details along with the total quantity ordered for each product:")
        cursorObject = dataBase.cursor()

        # Correct multi-line SQL query
        query = """
        SELECT p.productCode, p.productName, SUM(od.quantityOrdered) AS totalQuantityOrdered
	FROM products p
	JOIN orderdetails od ON p.productCode = od.productCode
	GROUP BY p.productCode, p.productName
	ORDER BY totalQuantityOrdered DESC;



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
