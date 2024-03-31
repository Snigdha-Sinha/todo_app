from Todo import TodoApp

def main() -> None:
    """
    Create an instance of the TodoApp class and start the application.
    """
    app: TodoApp = TodoApp()
    app.start()

if __name__ == "__main__":
    main()
