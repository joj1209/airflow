import pendulum
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg2",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 6, 10, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_5"],
    # params={"example_key": "example_value"},
) as dag:
    
    @task(task_id='python_xcom_push_by_return')
    def python_push1(**kwargs):
        return 'Success'
    
    @task(task_id='python_xcom_pull_1')
    def python_push2(**kwargs):
        ti = kwargs['ti']
        value1 = t1.xcom_pull(task_ids='python_xcom_push_by_return')
        print('xcom_pull 메서드로 직접 찾은 리턴 값:' + value1)
        
    @task(task_id='python_xcom_pull_2')
    def python_push2(status, **kwargs):
        print('함수 입력값으로 받은 값:' + status)     