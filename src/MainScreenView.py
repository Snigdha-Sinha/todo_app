from TaskView import TaskView
from ModifyView import ModifyScreenView

class MainScreenView(TaskView, ModifyScreenView):
    """
    contains function which displays the main menu when the todo app is started
    """
    def __init__(self) -> None:
        """
        initialises the parent class attributes
        """
        super().__init__()

    def display_main_menu(self) -> None:
        """
        displays the startup menu for the app
        with all the options which can be used by user
        """
        menu_string = '''
        What do you want to do?   
        1. Add a new task
        2. Modify an existing task
        3. Delete a task
        4. View the Todo list
        5. Quit
        \033[33mEnter choice (1/2/3/4/5): \033[0m
        '''
        print(menu_string,end=" ")