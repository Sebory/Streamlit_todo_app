import sqlite3

# let create db and its table and connect it

conn = sqlite3.connect("data1.db", check_same_thread=False, timeout=1)
c = conn.cursor()

# Database
# Table
# Fields/Columns
# DataType

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS taskstable(
        task TEXT, 
        task_status TEXT, 
        task_due_date DATE)""")

def add_data(task, task_status, task_due_date):
    c.execute("INSERT INTO taskstable(task, task_status, task_due_date) VALUES(?,?,?)", (task, task_status, task_due_date))
    conn.commit()

def view_all_data():
    c.execute("SELECT * FROM taskstable")
    data = c.fetchall()
    return data

def view_unique_tasks():
    c.execute("SELECT DISTINCT Task FROM taskstable")
    data = c.fetchall()
    return data

def get_task(task):
    c.execute(f"SELECT * FROM taskstable WHERE Task ='{task}'")
    data = c.fetchall()
    return data

def edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date):
    c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_task(task):
    c.execute(f"DELETE FROM taskstable WHERE task='{task}'")
    conn.commit()


