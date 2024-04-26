class Task:
    def __init__(self,task_name:str,category: str,due_date: str, priority: str) -> None:

        self.task_name = task_name
        self.category = category
        self.is_completed = False
        self.due_date = due_date
        self.priority = priority

    def modify_task_name(self,new_task_name: str) -> None:
        self.task_name = new_task_name

    def modify_category(self,new_category: str) -> None:
        self.category = new_category

    def modify_is_completed(self) -> None:
        self.is_completed = True

    def modify_due_date(self,new_due_date: str) -> None:
        self.due_date = new_due_date

    def modify_priority(self,new_priority: str) -> None:
        self.priority = new_priority