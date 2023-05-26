import mariadb
from dbcreds import host, port, user, password, database

user = "root"
password = "password"
host = "localhost"
port = 3306  
database = "python2"
cursor = conn.cursor()

# Execute the stored procedure
cursor.callproc("get_all_items")

# Fetch the results
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Print or process the results as needed