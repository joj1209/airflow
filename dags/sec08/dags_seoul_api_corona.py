from operators.seoul_api_to_csv_operator import SeoulApliToCsvOperator
from airflow import DAG
import pendulum

with DAG(
    dag_id="dags_seoul_api_corona", 
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_8"],
    # params={"example_key": "example_value"},
) as dag:
    
    '''서울시 코로나19 확진자 발생동향'''
    tb_corona19_count_status = SeoulApliToCsvOperator(
        task_id='tb_corona19_count_status',
        dataset_nm='TbCorona19CountStatus',
        path='/opt/airflow/files/TbCorona19CountStatus/{{ data_interval_end.in_timezone("Asia/Seoul") | ds_nodash }}',
        file_name='TbCorona19CountStatus.csv'
    )
    
    '''서울시 코로나19 백신 예방접종 현황'''
    tb_corona19_vaccine_stat_new = SeoulApliToCsvOperator(
        task_id='tb_corona19_vaccine_stat_new',
        dataset_nm='tvCorona19VaccinestatNew',
        path='/opt/airflow/files/tvCorona19VaccinestatNew/{{ data_interval_end.in_timezone("Asia/Seoul") | ds_nodash }}',
        file_name='tvCorona19VaccinestatNew.csv'
    )
    
    tb_corona19_count_status >> tb_corona19_vaccine_stat_new