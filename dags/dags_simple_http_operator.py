import pendulum
from airflow import DAG
from airflow.operators.bash import BaseOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_simple_http_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["airflow_pj","section_7"],
    # params={"example_key": "example_value"},
) as dag:
    
    '''서울시 공공자전거 대여소 정보'''
    tb_cycle_station_info = SimpleHttpOperator(
        task_id='tb_cycle_station_info',
        http_conn_id='openapi.seoul.go.kr',
        endpoint='{{var.value.apikey_openapi_seoul_go_kr}}/jdbc/tbCycleStationInfo/1/10',
        method='GET',
        headers={'Content-Type': 'application/json',
                'charset': 'utf-8',
                'Accept': '*/*'}
    )
    
    @task(task_id='python_2')
    def python_2(**kwargs):
        ti = kwargs['ti']
        rslt = ti.xcom_pull(task_ids='tb_cycle_station_info')
        # print(kwargs)
        # print(rslt)
        import json
        from pprint import pprint
        
        pprint(json.loads(rslt))
        
    tb_cycle_station_info >> python_2()