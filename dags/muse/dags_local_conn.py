import datetime
import pendulum
import psycopg2
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


def execute_query_with_psycopg(my_query, **kwargs):
    print(my_query)  # 'value_1'
    conn_args = dict(
        host='',
        user='',
        password='',
        dbname='',
        port=5432)
    conn = psycopg2.connect(**conn_args)
    cur = conn.cursor()
    cur.execute(my_query)

    for row in cur:
        print(row)
        
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
    
    t1