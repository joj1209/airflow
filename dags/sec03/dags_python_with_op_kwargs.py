import datetime
import pendulum
import random
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["airflow_pj"],
    # dagrun_timeout=datetime.timedelta(minutes=60),    
    # params={"example_key": "example_value"},
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id = 'regist2_t1',
        python_callable=regist2,
        op_args=['bskim','man','kr','seoul'],
        op_kwargs={'email':'joj@naver.com','phone':'010'}
    )
    
    regist2_t1