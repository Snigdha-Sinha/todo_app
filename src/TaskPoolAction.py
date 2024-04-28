from Task import Task

class TasksPool():
    def __init__(self) -> None:
        self.pending_tasks = []
        self.completed_tasks = []

class TasksPoolAction(TasksPool):
    def __init__(self) -> None:
        super().__init__()

    def add_task(self,task: Task) -> None:
        self.pending_tasks.append(task)

    def remove_task(self,task_number: int) -> None:
        if 1 <= task_number <= len(self.pending_tasks):
            self.pending_tasks.pop(task_number-1)
            print(f'Task {task_number} deleted from todo list')
        else:
            print("Please enter a valid task number")

    def shift_task(self, task_number: int) -> None:
        removed_task = self.pending_tasks.pop(task_number-1)
        self.completed_tasks.append(removed_task)

    def modify_task(self,task_number: int,prop_number: int,changed_value: str) -> None: 
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