import datetime
import pendulum
import psycopg2
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

def execute_query_with_psycopg(my_query, **kwargs):
    print(my_query)  # 'value_1'
    conn_args = dict(
        host='192.168.1.56',
        user='muse',
        password='muse',
        dbname='muse',
        port=3306)
    conn = psycopg2.connect(**conn_args)
    cur = conn.cursor()
    cur.execute(my_query)

    for row in cur:
        print(row)
    
sql_select_table = """select * from td_dbms_api_s;"""  
        
with DAG(
    dag_id="dags_local_conn",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["muse"],
    params={"example_key": "example_value"},
) as dag:  
    
    t1 = EmptyOperator(
        task_id="t1"
    )
    
    t2 = PythonOperator(
        task_id="test2_task",
        python_callable=execute_query_with_psycopg,
        op_kwargs={"my_query": 'select 1'})
    
    t3 = MySqlOperator(
        task_id="MySqlOperator",
        mysql_conn_id="conn_mysql",
        sql=sql_select_table        
    )
    
    t1 >> t2 >> t3