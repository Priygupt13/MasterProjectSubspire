import vanna
from vanna.remote import VannaDefault
vanna_model_name = "subspire_rag"
import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
vn = VannaDefault(model=vanna_model_name, api_key="1e346debc7bd4861b2a9ac8ece05dcbd")

# Connection details
conn_details = {
    "database_name": "",
    "server": "",
    "port": '',
    "user": "",
    "pwd": ""
}

# Creating connection string
conn_str = f"mysql://{conn_details['user']}:{conn_details['pwd']}@{conn_details['server']}:{conn_details['port']}/{conn_details['database_name']}"

# Creating engine
engine = create_engine(conn_str)

# You define a function that takes in a SQL query as a string and returns a pandas dataframe
def run_sql(sql: str) -> pd.DataFrame:
    df = pd.read_sql_query(sql, engine)
    return df

# This gives the package a function that it can use to run the SQL
vn.run_sql = run_sql
vn.run_sql_is_set = True

# The information schema query may need some tweaking depending on your database. This is a good starting point.
df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

plan = vn.get_training_plan_generic(df_information_schema)
print(plan)

#vn.train(plan=plan)

training_data = vn.get_training_data()
print(training_data)

#vn.train(question='Register a new user named Emily. She resides in the zip code 90210 and uses the email emily@example.com.', sql='INSERT INTO users (uuid, email, fullname, zipcode) VALUES ("e7b5cdef-025e-4e5a-9b71-9e8e201d0d01", "emily@example.com", "Emily", "90210")')



training_data = vn.get_training_data()
print(training_data)