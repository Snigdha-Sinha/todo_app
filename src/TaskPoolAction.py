from Task import Task

class TasksPool():
    """
    contains constructor to initialise empty lists for
    pending tasks and completed tasks
    """
    def __init__(self) -> None:
        """
        initialises the attributes for the TasksPool class object
        an empty list is initialised for pending tasks as well as completed tasks
        """
        self.pending_tasks = []
        self.completed_tasks = []

class TasksPoolAction(TasksPool):
    """
    contains functions to handle all the features of the todo app
    (adding a task, removing task, modifying an existing task)
    """
    def __init__(self) -> None:
        super().__init__()

    def add_task(self,task: Task) -> None:
        """
        append a task to the pending task list

        : param task: an object of the Task class which contains all attributes of a task
        : type task: Task
        """
        self.pending_tasks.append(task)

    def remove_task(self,task_number: int) -> None:
        """
        if a valid task number is provided from the pending task list, 
        it is removed from the list
        if an invalid task number is provided, user is prompted to enter a valid one

        : param task_number: the serial number of the task to be removed
        : type task_number: int
        """
        if 1 <= task_number <= len(self.pending_tasks):
            self.pending_tasks.pop(task_number-1)
            print(f'\033[32mTask {task_number} deleted from todo list\033[0m')
        else:
            print("\033[31mPlease enter a valid task number\033[0m")

    def shift_task(self, task_number: int) -> None:
        """
        function called when the completion status of a task changes
            - it is marked as completed
            - removed from the pending tasks list
            - appended to the completed tasks list

        : param task_number: the serial number of the task to be marked as completed
        : type task_number: int
        """
        removed_task = self.pending_tasks.pop(task_number-1)
        self.completed_tasks.append(removed_task)

    def modify_task(self,task_number: int,prop_number: int,changed_value: str) -> None: 
        """
        modifies a particular property of a particular task (both specified by user)

        : param task_number: the serial number of the task to be modified
        : type task_number: int

        : param prop_number: the serial number of the property to be modified for the task
        : type prop_number: int

        : param changed_value: the new modified value for the particular property of the task
        : type changed_value: str
        """
        task_to_modify = self.pending_tasks[task_number-1]
        if prop_number == 1:
            task_to_modify.modify_task_name(changed_value)
        elif prop_number == 2:
            task_to_modify.modify_category(changed_value)
        elif prop_number == 3:
            task_to_modify.modify_is_completed()
            self.shift_task(task_number)
        elif prop_number == 4:
            task_to_modify.modify_due_date(changed_value)
        else:
            task_to_modify.modify_priority(changed_value)