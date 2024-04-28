from TaskView import TaskView
from ModifyView import ModifyScreenView

class MainScreenView(TaskView, ModifyScreenView):
    def __init__(self) -> None:
        super().__init__()

    def display_main_menu(self) -> None:
        menu_string = '''
        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        Enter choice (1/2/3/4/5):
        '''
        print(menu_string,end=" ")