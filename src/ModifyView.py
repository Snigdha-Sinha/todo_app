class ModifyScreenView:
    def display_modify_menu(self) -> None:

        modify_string = '''
        What do you want to modify?
        1. Task Name
        2. Category
        3. Completion Status
        4. Due Date
        5. Priority
        Enter choice (1/2/3/4/5): 
        '''
        print(modify_string, end = " ")
        
    def display_tasks(self) -> None:
        for index,task in enumerate(self.pending_tasks, start = 1):
            print(f'Task {index}: {task.task_name}')