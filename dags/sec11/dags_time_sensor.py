import pendulum
from airflow import DAG
from airflow.sensors.date_time import DateTimeSensor

with DAG(
    dag_id="dags_time_sensor",
    start_date=pendulum.datetime(2024, 7, 1, 0, 0, 0),
    end_date=pendulum.datetime(2024, 7, 1, 1, 0, 0),
    schedule="*/10 * * * *",
    catchup=True,
    tags=["airflow_pj","section_11"],
) as dag:
    sync_sensor = DateTimeSensor(
        task_id='sync_sensor',
        target_time="""{{ macros.datetime.utcnow() + macros.timedelta(minutes=5)}}""",
    )