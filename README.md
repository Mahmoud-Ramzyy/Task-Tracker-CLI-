# Task Tracker CLI

A simple command-line task tracker built with Python and Click. This application allows users to manage tasks directly from the terminal by adding, updating, deleting, listing, and tracking task progress. All tasks are stored locally in a JSON file for persistence between sessions.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* List all tasks
* Filter tasks by status
* Mark tasks as **in progress**
* Mark tasks as **done**
* Store tasks persistently using JSON
* Track creation and update timestamps

## Technologies Used

* Python 3
* Click (for CLI commands)
* JSON (for data storage)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

### 2. Install dependencies

```bash
pip install click
```

## Usage

Run the application:

```bash
python task_tracker.py
```

### Add a Task

```bash
python task_tracker.py add "Learn Python"
```

Output:

```bash
Task added successfully (ID: 1)
```

### List All Tasks

```bash
python task_tracker.py list
```

### List Tasks by Status

Todo tasks:

```bash
python task_tracker.py list todo
```

In-progress tasks:

```bash
python task_tracker.py list in-progress
```

Done tasks:

```bash
python task_tracker.py list done
```

### Update a Task

```bash
python task_tracker.py update 1 "Learn Advanced Python"
```

### Delete a Task

```bash
python task_tracker.py del 1
```

### Mark a Task as In Progress

```bash
python task_tracker.py mark-in-progress 1
```

### Mark a Task as Done

```bash
python task_tracker.py mark-done 1
```

### Clear All Tasks

```bash
python task_tracker.py clr
```

## Data Structure

Tasks are stored in a `tasks.json` file in the following format:

```json
{
  "id": 1,
  "task": "Learn Python",
  "status": "todo",
  "createdAt": "2025-06-03 14:30:00",
  "updatedAt": null
}
```
## Demo

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Project Structure

```text
task-tracker-cli/
│
├── task_tracker.py
├── tasks.json
└── README.md
```

## Future Improvements

* Task priorities
* Due dates
* Search functionality
* Export tasks to CSV
* Colored terminal output
* Unit testing

## Author

Developed by [Mahmoud Ramzy]

## License

This project is open source and available under the MIT License.
