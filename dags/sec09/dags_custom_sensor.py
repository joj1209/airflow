from sensors.seoul_api_date_sensor import SeoulApiDateSensor
from airflow import DAG
import pendulum

with DAG(
    dag_id="dags_custom_sensor",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_9"],
    # params={"example_key": "example_value"},
) as dag:
    tb_corona_19_count_status_sensor = SeoulApiDateSensor(
        task_id='tb_corona_19_count_status_sensor',
        dataset_nm='TbCorona19CountStatus',
        base_dt_col='S_DT',
        day_off=0,
        poke_interval=600,
        mode='reschedule'
    )
    
    tv_corona19_vaccine_stat_new_sensor = SeoulApiDateSensor(
        task_id='tv_corona19_vaccine_stat_new_sensor',
        dataset_nm='tvCorona19VaccinestatNew',
        base_dt_col='S_VC_DT',
        day_off=-1,
        poke_interval=600,
        mode='reschedule'
    )