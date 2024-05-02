class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        if not task:
            raise ValueError("Task cannot be empty")
        if task in self.tasks:
            raise ValueError("Task already exists")
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def start(self):
        while True:
            user_input = input("> ")
            if user_input == "1":
                self.add_task(input("Enter task: "))
            elif user_input == "2":
                for task in self.get_tasks():
                    print(task)
            elif user_input == "3":
                break
            else:
                print("Invalid input")