from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

dag1 = DAG(dag_id = "first_dag", start_date = datetime(2026,8,21), catchup = False)

def hello():
    print("Hello from Task1")

def hello2():
    print("Hello from Task2")

task1 = PythonOperator(task_id = "task_1", python_callable = hello, dag = dag1)

task2 = PythonOperator(task_id = "task_2", python_callable = hello2, dag = dag1)

task1 >> task2