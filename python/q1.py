# importing required library 
import mysql.connector 

# connecting to the database 
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="db1"
) 

# preparing a cursor object 
cursorObject = dataBase.cursor()

# selecting query
query = """
SELECT p.productCode, p.productName, pl.textDescription 
FROM products p
JOIN productlines pl ON p.productLine = pl.productLine;
"""

# Execute the query
cursorObject.execute(query)

# Fetch all the results
myresult = cursorObject.fetchall()

# Print each result
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()
