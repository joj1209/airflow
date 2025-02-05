import pendulum
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 6, 10, tz="Asia/Seoul"),
    catchup=True,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_5"],
    # params={"example_key": "example_value"},
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)
    
    show_templates()