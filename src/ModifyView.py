class ModifyScreenView:
    def display_modify_menu(self) -> None:
        """
        displays the menu for the modification option of the Todo App
        """

        modify_string = '''
        What do you want to modify?
        1. Task Name
        2. Category
        3. Completion Status
        4. Due Date
        5. Priority
        \033[33mEnter choice (1/2/3/4/5): \033[0m
        '''
        print(modify_string, end = " ")
        
    def display_tasks(self) -> None:
        """
        displays tasks according to serial number
        so that user can choose which one to modify/remove
        """
        for index,task in enumerate(self.pending_tasks, start = 1):
            print(f'Task {index}: {task.task_name}')