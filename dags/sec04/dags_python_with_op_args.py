import datetime
import pendulum
import random
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["airflow_pj","section_4"],
    # dagrun_timeout=datetime.timedelta(minutes=60),    
    # params={"example_key": "example_value"},
) as dag:
    
    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable=regist,
        op_args=['bskim','man','kr','seoul']
    )
    
    regist_t1