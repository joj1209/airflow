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
    dag_id="dags_python_with_trigger_rule_eg2",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_6"],
    # params={"example_key": "example_value"},
) as dag:
    
    @task.branch(task_id='python_branch_task')
    def random_branch():
        import random
        
        item_lst = ['A','B','C']
        selected_item = random.choice(item_lst)
        if selected_item == 'A':
            return 'task_a'
        elif selected_item == 'B':
            return 'task_b'
        elif selected_item == 'C':
            return 'task_c'
        
    task_a = BashOperator(
        task_id = 'task_a',
        bash_command='echo upstream1'
    )
    
    @task(task_id='task_b')
    def task_b():
        print('정상 처리')

    @task(task_id='task_c')
    def task_c():
        print('정상 처리')
        
    @task(task_id='task_d', trigger_rule='none_skipped')
    def task_d():
        print('정상 처리')

    random_branch() >> [task_a, task_b(), task_c()] >> task_d()
