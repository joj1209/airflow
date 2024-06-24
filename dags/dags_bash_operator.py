import datetime
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    
        # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    
    t1 = EmptyOperator(
        task_id="t1"
    )
    
    t2 = EmptyOperator(
        task_id="t2"
    )
    
    t3 = EmptyOperator(
        task_id="t3"
    )
    
    t4 = EmptyOperator(
        task_id="t4"
    )
    
    t5 = EmptyOperator(
        task_id="t5"
    )
    
    t6 = EmptyOperator(
        task_id="t6"
    )
    
    t7 = EmptyOperator(
        task_id="t7"
    )
    
    t8 = EmptyOperator(
        task_id="t8"
    )
    
    bash_t1 >> bash_t2
    
    t1 >> [t2,t3] >> t4
    t5 >> t4
    [t4,t7] >> t6 >> t8