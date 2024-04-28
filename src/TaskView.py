class TaskView:
    def display_pending_task(self) -> None:
        print("PENDING TASKS: ")
        if len(self.pending_tasks) == 0:
            print("Yay! you have no pending tasks")
        else:
            for index, task in enumerate(self.pending_tasks, start=1):
                    print()
                    print(f'Task {index}:')
                    print(f'Task: {task.task_name}')
                    print(f'Category: {task.category}')
                    print(f'Due Date: {task.due_date}')
                    print(f'Priority: {task.priority}')

    def display_completed_task(self) -> None:
        print("================= \n")
        print("COMPLETED TASKS: ")
        if len(self.completed_tasks) == 0:
            print("Oops.. you haven't finished any task")
        else:
            for index, task in enumerate(self.completed_tasks, start=1):
                    print()
                    print(f'Task {index}:')
                    print(task.task_name)
                    print(task.category)
                    print(task.due_date)
                    print(task.priority)