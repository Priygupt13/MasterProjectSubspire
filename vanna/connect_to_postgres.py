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
table_data = []

for table in tables:
    table_name = table[0]
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    column_names = [column[0] for column in columns]
    table_data.append({table_name: column_names})

# Print table data
print("\nTable data:")
for data in table_data:
    print(data)

# Close the connection
conn.close()
