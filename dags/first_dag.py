from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    description='My first simple DAG',
    schedule_interval='@daily',
)

t1 = EmptyOperator(
    task_id='task1',
    dag=dag,
)

t2 = EmptyOperator(
    task_id='task2',
    dag=dag,
)

t1 >> t2