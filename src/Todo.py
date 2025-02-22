from Task import Task
from TaskPoolAction import TasksPoolAction
from MainScreenView import MainScreenView

class TodoApp(TasksPoolAction,MainScreenView):
    def __init__(self) -> None:

        TasksPoolAction.__init__(self)
        MainScreenView.__init__(self)

    def handle_modification(self,prop_to_modify: int) -> str:
        if prop_to_modify == 1:
            new_task_name = input("Enter new task name: ")
            return new_task_name
        
        elif prop_to_modify == 2:
            new_category = input("Enter new category: ")
            return new_category
        
        elif prop_to_modify == 3:
            return "change status"
        
        elif prop_to_modify == 4:
            new_due_date = input("Enter new due date: ")
            return new_due_date
        
        else:
            new_priority = input("Enter new priority: ")
            return new_priority
        
        
    def start(self) -> None:
        while True:
            self.display_main_menu()
            input_choice = int(input())

            if input_choice == 1:
                task_name = input("Enter task name: ")
                category = input("Enter category: ")
                due_date = input("Enter due date: ")
                priority = input("Enter priority: ")
                task = Task(task_name,category,due_date,priority)
                self.add_task(task)
                print("Task added successfully")

            elif input_choice == 2:
                self.display_tasks()
                task_to_modify = int(input("enter task number to be modified: "))
                if 1 <= task_to_modify <= len(self.pending_tasks):
                    self.display_modify_menu()
                    prop_to_modify = int(input())
                    changed_value = self.handle_modification(prop_to_modify)
                    self.modify_task(task_to_modify,prop_to_modify,changed_value)
                    print("Task modified successfully")
                else:
                    print("Please enter valid choice")

            elif input_choice == 3:
                if len(self.pending_tasks)>0:
                    self.display_tasks()
                    task_number = int(input("Enter task number to delete: "))
                    self.remove_task(task_number)
                else:
                    print("No tasks left to delete..")

            elif input_choice == 4:
                self.display_pending_task()
                self.display_completed_task()

            elif input_choice == 5:
                print("Exiting.. ")
                break

            else:
                print("Invalid choice.. please try again")
    

        
    
