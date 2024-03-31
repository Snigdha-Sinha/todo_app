class Task:
    """
    contains functions to handle the feature of modifying a task
    separate functions perform separate cases of modifying 
    task name, category, completion status, due date and priority
    """
    def __init__(self,task_name:str,category: str,due_date: str, priority: str) -> None:
        """
        initialises all necessary attributes for the Task class object

        : param task_name: name of the task
        : type task_name: str

        : param category: category of the task
        : type category: str

        : param due_date: due date of the task
        : type category: str

        : param priority: priority of the task
        : type priority: str
        """

        self.task_name = task_name
        self.category = category
        self.is_completed = False
        self.due_date = due_date
        self.priority = priority

    def modify_task_name(self,new_task_name: str) -> None:
        """
        modify the task name and change it to the new task name provided to the function

        : param new_task_name: new task name which replaces the existing one
        : type new_task_name: str
        """
        self.task_name = new_task_name

    def modify_category(self,new_category: str) -> None:
        """
        modify the category and change it to the new category provided to the function

        : param new_category: new category which replaces the existing one
        : type new_category: str
        """
        self.category = new_category

    def modify_is_completed(self) -> None:
        """
        modify the completion status of the task
        when a task is created, its completion status is False
        if this function is called, the completion status changes to True
        """
        self.is_completed = True

    def modify_due_date(self,new_due_date: str) -> None:
        """
        modify the due date and change it to the new due date provided to the function

        : param new_due_date: new due date which replaces the existing one
        : type new_due_date: str
        """
        self.due_date = new_due_date

    def modify_priority(self,new_priority: str) -> None:
        """
        modify the priority and change it to the new priority provided to the function

        : param new_priority: new priority which replaces the existing one
        : type new_priority: str
        """
        self.priority = new_priority