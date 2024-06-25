import datetime
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    
        # [START howto_operator_bash]
    t1_orange = BashOperator(
        task_id="t1_orange",
        # bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
        bash_command="/opt/airflow/plugins/select_fruit.sh ORANGE",
    )
    
    t1_avocado = BashOperator(
        task_id="t1_avocado",
        # bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
        bash_command="/opt/airflow/plugins/select_fruit.sh AVOCADO",
    )
    
    t1_orange >> t1_avocado
    