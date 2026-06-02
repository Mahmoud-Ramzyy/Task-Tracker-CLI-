from datetime import datetime
import click
import json

tasks= []   

# --------  saving and loading tasks in/from json file ---------------
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# =============================  CLI config ========================
@click.group()
def cli():
    """Task Tracker CLI App"""
    pass

#------- load the content of tasks from the last sessions -----------------
tasks = load_tasks()

# ======================== Add function =========================
@click.command(name="add")
@click.argument("t")
def add_task(t):
    '''Add tasks here:'''
    count = tasks[-1]["id"] + 1 if tasks else 1 # get the last task number
    
    current= datetime.now().strftime("%Y-%m-%D %H:%M:%S")
    
    task={"id":count, "task":t,
            "status":"todo",
            "createdAt":current,
            "updatedAt":None}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {count})")
    
#========================= list function ============================
@click.command(name='list')
@click.argument('st', required=False)
def list_tasks(st=None):
    '''List all the required tasks details'''
    if not tasks:
        print("No tasks yet")
        return
    for task in tasks:
        if st is None or task['status'] == st:
            print("         -------------------------------")
            print(f"Task{task['id']}: {task['task']}")
            print(f'status:{task["status"]}')
            print(f'Created at: {task["createdAt"]}')
            if task["updatedAt"]:
                print(f'Updated at: {task["updatedAt"]}')

#========================= Delete function  ============================
@click.command(name='del')
@click.argument('id',type=int)
def delete_task(id):
    '''Delete certain task from the list'''
    task = get_task(id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
    else:
        print("Task not found")

#============================ Update function ======================================
@click.command(name='update')
@click.argument('id',type=int)
@click.argument('task')
def update_task(id,task):
    '''update the task details'''
    current= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for t in tasks:
        if t['id'] == id:
            t['task'] = task
            t['updatedAt'] = current
            save_tasks(tasks)  # update the json file 
            break
    else:
        print("there's no such task in the list")

#================================ Mark functions ======================
@click.command(name='mark-in-progress')
@click.argument('id',type=int)
def inprogress_task(id):
    current= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for t in tasks:
        if t['id'] == id:
            t['status'] = 'in-progress'
            t['updatedAt'] = current
            save_tasks(tasks)  # update the json file 
            break
    else:
        print("there's no such task in the list")
                #=======================================================
@click.command(name='mark-done')
@click.argument('id',type=int)
def done_task(id):
    current= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for t in tasks:
        if t['id'] == id:
            t['status'] = 'done'
            t['updatedAt'] = current
            save_tasks(tasks)  # update the json file 
            break
    else:
        print("there's no such task in the list")
#================================ Helpful functions =============================
def get_task(id):
    return next((t for t in tasks if t["id"] == id), None)

#=========================== clear the list =============================
@click.command(name='clr')
def clear_tasks():
    tasks=[]
    save_tasks(tasks)
# ================================ CLI instructions =============================
cli.add_command(add_task)
cli.add_command(list_tasks)
cli.add_command(delete_task)
cli.add_command(update_task)
cli.add_command(inprogress_task)
cli.add_command(done_task)
cli.add_command(clear_tasks)

if __name__ == "__main__":
    cli()
