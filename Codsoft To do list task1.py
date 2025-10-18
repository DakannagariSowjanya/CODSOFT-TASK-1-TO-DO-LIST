def display_task(tasks):
    if tasks:
        n = len(tasks)
        for i in range(n):
            task = tasks[i]
            print(f"{i+1}. {task}")
    else:
        print("No tasks are avaiable here")

def add_task(tasks):
    s = input("Enter a task to be added: ").strip(" ")
    m = len(s)
    if m > 0:
        tasks.insert(len(tasks), s)
        print("Task is added")
    else:
        print("Task cannot be empty")

def remove_task(tasks):
    display_task(tasks)
    n = input("Enter task number to delete: ").strip("")
    
    if not n.isdigit():
        print("Please give a valid integer number")
        return

    n = int(n)
    if n > 0 and n <= len(tasks):
        rem_it = tasks[n - 1]
        del tasks[n - 1]
        print("Removed:", rem_it)
    else:
        print("Invalid task number")
def update_task(tasks):
    display_task(tasks)
    n = input("Enter task number to update: ").strip("")
    
    if not n.isdigit():
        print("Please give a valid integer number")
        return

    n = int(n)
    if n > 0 and n <= len(tasks):
        new_tsk = input("Enter new task which you want to modify: ").strip(" ")
        if len(new_tsk) > 0:
           tasks[n - 1] = new_tsk
           print("Your Task was got updated")
        else:
           print("Task cannot be empty")
    else:
        print("Invalid task number")
        

def menu():
    tasks = []
    while True:
        print("\n___TO_DO_LIST___")
        print("1) Show tasks")
        print("2) Add task")
        print("3) Delete task")
        print("4) update task")
        print("5) Exit")

        ch = input("Choice: ").strip(" ")
        if ch == "1":
            display_task(tasks)
        elif ch == "2":
            add_task(tasks)
        elif ch == "3":
            remove_task(tasks)
        elif ch == "4":
            update_task(tasks)
        elif ch == "5":
            break
        else:
            print("Invalid choice")

    print("_____END OF TASK ___")

def main():
    menu()

main()
