import datetime
import pendulum

from airflow import DAG
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:

    send_email_task = EmailOperator(
        task_id="send_email_task",
        to='joj1209@naver.com',
        subject='Airflow 성공메일'
        html_content='Airflow 작업이 완료됨'
    )
