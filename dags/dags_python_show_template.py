import datetime
import pendulum
import random
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_show_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 6, 10, tz="Asia/Seoul"),
    catchup=True,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj"],
    # params={"example_key": "example_value"},
) as dag:
    
    def select_fruit():
        fruit = ['APPLE','BANANA','ORANGE','AVOCADO']
        rand_init = random.randint(0,3)
        print(fruit[rand_init])

    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable=select_fruit
    )
    
    py_t1