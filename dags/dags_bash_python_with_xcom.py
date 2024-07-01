import datetime
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_bash_python_with_xcom",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_5"],
    # params={"example_key": "example_value"},
) as dag:
    
    @task(task_id='python_push')
    def python_push_xcom(**kwargs):
        result_dict = {'state':'Good','data':[1,2,3],'options_cnt':100}
        return result_dict

    bash_pull = BashOperator(
        task_id="bash_pull",
        env={'STATUS':"{{ ti.xcom_pull(task_ids='python_push')["status"]}}",
            'DATA':"{{ ti.xcom_pull(task_ids='python_push')["data"]}}",
            'OPTION_CNT':"{{ ti.xcom_pull(task_ids='python_push')["option_cnt"]}}"},
        bash_command="echo $STATUS && echo $DATA && echo $OPTION_CNT",
        do_xcom_push=False
    )

    bash_push = BashOperator(
        task_id="bash_push",
        bash_command='echo PUSH_START '
                    '{{ ti.xcom_push(key='bash_pushed',value=200) }} &&'
                    'echo COMPLETE'
    )

    @task(task_id='python_pull')
    def python_pull_xcom(**kwargs):
        ti = kwargs['ti']
        status_value = ti.xcom_pull(key='bash_pushed')
        return_value = ti.xcom_pull(task_id='bash_push')
        print('status_value:' + str(status_value))
        print('return_value:' + return_value)
    
    bash_push >> python_pull_xcom()
