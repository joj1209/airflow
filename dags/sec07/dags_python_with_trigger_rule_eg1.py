import datetime
import pendulum
import random
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.exceptions import AirflowException

import pendulum

with DAG(
    dag_id="dags_python_with_trigger_rule_eg1",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_6"],
    # params={"example_key": "example_value"},
) as dag:
    
    bash_upstream_1 = BashOperator(
        task_id = 'bash_upstream_1',
        bash_command='echo upstream1'
    )
    
    @task(task_id='python_upstream_1')
    def python_upstream_1():
        raise AirflowException('downstream_1 Exception!')
    
    @task(task_id='python_upstream_2')
    def python_upstream_2():
        print('정상 처리')
        
    @task(task_id='python_downstream_1', trigger_rule='all_done')
    def python_downstream_1():
        print('정상 처리')
        
    [bash_upstream_1, python_upstream_1(), python_upstream_2()] >> python_downstream_1()
