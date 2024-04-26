class TaskView:
    def display_pending_task(self) -> None:
        print("\033[46mPENDING TASKS: \033[0m")
        if len(self.pending_tasks) == 0:
            print("Yay! you have no pending tasks")
        else:
            for index, task in enumerate(self.pending_tasks, start=1):
                    print()
                    print(f'\033[1;31;40mTask {index}:\033[0m')
                    print(f'Task: {task.task_name}')
                    print(f'Category: {task.category}')
                    print(f'Due Date: {task.due_date}')
                    print(f'Priority: {task.priority}')

    def display_completed_task(self) -> None:
        print("================= \n")
        print("\033[46mCOMPLETED TASKS: \033[0m")
        if len(self.completed_tasks) == 0:
            print("Oops.. you haven't finished any task")
        else:
            for index, task in enumerate(self.completed_tasks, start=1):
                    print()
                    print(f'\033[1;31;40mTask {index}:\033[0m')
                    print(task.task_name)
                    print(task.category)
                    print(task.due_date)
                    print(task.priority)