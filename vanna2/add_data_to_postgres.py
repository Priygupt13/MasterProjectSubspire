from vanna.remote import VannaDefault
vanna_model_name = "subspire_rag"
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import mysql.connector
import psycopg2
def get_answer(question_from_user):
    pymysql.install_as_MySQLdb()
    vn = VannaDefault(model=vanna_model_name, api_key="1e346debc7bd4861b2a9ac8ece05dcbd")

    # Connection details
    conn_details = {
        "database_name": "",
        "server": "subspire.cluster-cegcie0qxdeo.us-west-1.rds.amazonaws.com",
        "port": 3306,
        "user": "robinhood",
        "pwd": ""
    }

    conn_str = f"mysql://{conn_details['user']}:{conn_details['pwd']}@{conn_details['server']}:{conn_details['port']}/{conn_details['database_name']}"
    engine = create_engine(conn_str)
    def run_sql(sql: str) -> pd.DataFrame:
        df = pd.read_sql_query(sql, engine)
        return df

    vn.run_sql = run_sql
    vn.run_sql_is_set = True

    df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

    plan = vn.get_training_plan_generic(df_information_schema)
    print(plan)

    # If you like the plan, then uncomment this and run it to train
    #vn.train(plan=plan)

    training_data = vn.get_training_data()
    print(training_data)

    #training_data = vn.get_training_data()
    #print(training_data)
    res = vn.add_data(question=question_from_user)
    print(res)
    sql = res
    is_data_manipulating_question = False

    if "INSERT" in res or "DELETE" in res or "UPDATE" in res:
        is_data_manipulating_question = True

    try:
        conn = mysql.connector.connect(
            host="subspire.cluster-cegcie0qxdeo.us-west-1.rds.amazonaws.com",
            database="subspire",
            user="robinhood",
            password="bluesky116",
            port=3306
        )
        print("Connected to the database")

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

    cursor = conn.cursor()
    sql = res

    try:
        cursor.execute(sql)

        if is_data_manipulating_question == True:
            result = "Data manipulated succesfully"
            conn.commit()

        else:
            rows = cursor.fetchall()
            result = []
            for row in rows:
                # Do something with each row
                result.append(row)

    except psycopg2.Error as e:
        print("Error manipulating data:", e)
        conn.rollback()
    # Close the connection
    conn.close()
    print("you are done")
    return result
