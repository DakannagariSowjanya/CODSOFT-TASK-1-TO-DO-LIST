
📝 To-Do List using Python

A simple command-line To-Do List application built using Python. This project allows users to create and manage a list of tasks directly through the terminal.

🚀 Features

- 📋 Display all tasks
- ➕ Add a new task
- 🗑️ Delete a task
- ✏️ Update an existing task
- ❌ Exit the application
- ✅ Validates task numbers before deleting or updating
- 🚫 Prevents empty tasks from being added

🛠️ Technologies Used

- Python 3
- Python Lists
- Functions
- Loops
- Conditional Statements
- User Input

📂 Project Structure

To-Do-List/
│
├── todo.py
└── README.md

▶️ How to Run

1. Clone the repository

git clone https://github.com/your-username/your-repository-name.git

2. Navigate to the project folder

cd your-repository-name

3. Run the Python program

python todo.py

💻 How It Works

When the program starts, a menu is displayed:

___TO_DO_LIST___
1) Show tasks
2) Add task
3) Delete task
4) update task
5) Exit

Choice:

1. Show Tasks

Displays all currently available tasks with their task numbers.

Example:

1. Complete Python practice
2. Solve DSA problems
3. Read a book

2. Add Task

The user can enter a new task.

Enter a task to be added: Complete Python practice
Task is added

The program also prevents empty tasks from being added.

3. Delete Task

The user enters the task number that needs to be deleted.

Enter task number to delete: 2
Removed: Solve DSA problems

The program checks whether the entered task number is valid.

4. Update Task

The user can replace an existing task with a new task.

Enter task number to update: 1
Enter new task which you want to modify: Practice Python functions
Your Task was got updated

The program also prevents an empty task from being entered.

5. Exit

Selecting option "5" exits the application.

_____END OF TASK ___

📚 Concepts Practiced

This project helped me practice fundamental Python concepts such as:

- Functions
- Lists
- "if-else" conditions
- "while" loops
- "for" loops
- User input using "input()"
- String methods
- List operations such as "insert()" and "del"
- Input validation using "isdigit()"

🔮 Future Improvements

Possible improvements for this project:

- Save tasks permanently using a file
- Add task completion status
- Add task priorities
- Add due dates
- Add a graphical user interface
- Store tasks using a database
