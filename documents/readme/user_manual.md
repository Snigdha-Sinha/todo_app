## Todo App User Manual
### Use Case - 1: Adding a Task

```
What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         1

Enter task name: write rst files
Enter category: work
Enter due date: 21.03
Enter priority: high
Task added successfully

        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         1
Enter task name: boil eggs
Enter category: personal
Enter due date: 20.03
Enter priority: low
Task added successfully
```

### Use Case - 2: Modifying a Task

```
What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         2
Task 1: write rst files
Task 2: boil eggs
Task 3: write architecture specification doc
enter task number to be modified: 1

        What do you want to modify?
        1. Task Name
        2. Category
        3. Completion Status
        4. Due Date
        5. Priority
        Enter choice (1/2/3/4/5): 
         1
Enter new task name: setup and render rst files
Task modified successfully

        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         2
Task 1: setup and render rst files
Task 2: boil eggs
Task 3: write architecture specification doc
enter task number to be modified: 2

        What do you want to modify?
        1. Task Name
        2. Category
        3. Completion Status
        4. Due Date
        5. Priority
        Enter choice (1/2/3/4/5): 
         3
Task modified successfully

        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         2
Task 1: setup and render rst files
Task 2: write architecture specification doc
enter task number to be modified: 2

        What do you want to modify?
        1. Task Name
        2. Category
        3. Completion Status
        4. Due Date
        5. Priority
        Enter choice (1/2/3/4/5): 
         4
Enter new due date: 25.03
Task modified successfully

        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         2
Task 1: setup and render rst files
Task 2: write architecture specification doc
enter task number to be modified: 1

        What do you want to modify?
        1. Task Name
        2. Category
        3. Completion Status
        4. Due Date
        5. Priority
        Enter choice (1/2/3/4/5): 
         5
Enter new priority: medium
Task modified successfully
```

### Use Case - 3: Deleting a Task

```
What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         3
Task 1: setup and render rst files
Task 2: write architecture specification doc
Enter task number to delete: 1
Task 1 deleted from todo list

        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         4

PENDING TASKS: 

Task 1:
Task: write architecture specification doc
Category: work
Due Date: 25.03
Priority: high
================= 

COMPLETED TASKS: 

Task 1:
boil eggs
personal
20.03
low
```

### Use Case - 4: Viewing the Todo List

```
What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3): 
         4
PENDING TASKS: 

Task 1:
Task: setup and render rst files
Category: work
Due Date: 21.03
Priority: medium

Task 2:
Task: write architecture specification doc
Category: work
Due Date: 25.03
Priority: high
================= 

COMPLETED TASKS: 

Task 1:
boil eggs
personal
20.03
low
```


