import mysql.connector

# Connect to the database
try:
    conn = mysql.connector.connect(
        host="subspire.cluster-cegcie0qxdeo.us-west-1.rds.amazonaws.com",
        user="robinhood",
        password="bluesky116",
        database="subspire",
        port=3306
    )
    print("Connected to the database")
except mysql.connector.Error as e:
    print("Error connecting to the database:", e)

# Get a cursor
cursor = conn.cursor()

# Get tables
cursor.execute("SHOW TABLES")

tables = cursor.fetchall()
print("Tables in the database:")

# Fetch and print data for each table
for table in tables:
    table_name = table[0]
    print("\nTable:", table_name)
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    print(column_names)  # Print column names
    for row in rows:
        print(row)  # Print each row

# Close the connection
conn.close()
