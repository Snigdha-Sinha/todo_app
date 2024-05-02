from Todo import TodoApp

def test_add_task():
    app = TodoApp()
    app.add_task("Task 1")
    assert len(app.tasks) == 1

def test_add_empty_task():
    app = TodoApp()
    with pytest.raises(ValueError):
        app.add_task("")

def test_add_duplicate_task():
    app = TodoApp()
    app.add_task("Task 1")
    with pytest.raises(ValueError):
        app.add_task("Task 1")