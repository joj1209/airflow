import pendulum
from airflow import DAG
from airflow.sensors.date_time import DateTimeSensor

with DAG(
    dag_id="dags_time_sensor",
    start_date=pendulum.datetime(2023, 5, 1, 0, 0, 0),
    end_date=pendulum.datetime(2023, 5, 1, 1, 0, 0),
    schedule="*/10 * * * *",
    catchup=True,
    tags=["airflow_pj","section_10"],
) as dag:
    sync_sensor = DateTimeSensor(
        task_id='sync_sensor',
        target_time="""{{ macros.datatime.utcnow() + macros.timedelta(minutes=5)}}""",
    )