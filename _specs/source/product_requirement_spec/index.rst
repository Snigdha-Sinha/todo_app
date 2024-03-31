****************************************
Product Requirement Specification
****************************************

Introduction
========================
The Product Requirement Specification document delineates the functional and non-functional requisites, use cases, constraints, and assumptions pertinent to the Menu-Driven Todo App. It serves as a guide for the development team to ensure adherence to specified requirements and the delivery of an intuitive user experience.

Functional Requirements
========================

Task Management
~~~~~~~~~~~~~~~~~~~~~~~~~
- Users must be capable of adding tasks to the todo list, specifying task attributes such as name, category, due date, and priority.
- Users should possess the ability to modify existing tasks, encompassing attributes such as task name, category, completion status, due date, and priority.
- The application must facilitate task deletion from the todo list.
- Users should be provided with the functionality to view both pending and completed tasks, distinctly.

Non-Functional Requirements
===========================
User Interface
~~~~~~~~~~~~~~~~~~~~~~~
- The user interface must exhibit intuitiveness and ease of navigation.
- Menu options must be distinctly labeled and easily accessible.

Performance
~~~~~~~~~~~~~~~~~~~~~~
- The application should exhibit prompt responsiveness to user actions, even with a substantial number of tasks listed.
- Task operations such as addition, modification, and deletion should be executed efficiently.

Reliability
~~~~~~~~~~~~~~~~~~~~~~~
- The application must gracefully handle errors and furnish informative error messages to users.
- Data integrity must be upheld, ensuring precise storage and retrieval of tasks.

Security
~~~~~~~~~~~~~~~~~~~~~~~~~
- Sensitive user data must not be stored within the application.
- Access to task management functionalities must be confined to authorized users exclusively.

Use Cases
========================
1. Adding a Task
~~~~~~~~~~~~~~~~~~~~~~~
- User initiates the addition of a new task.
- User furnishes task particulars such as name, category, due date, and priority.
- The system integrates the task into the todo list.

2. Modifying a Task
~~~~~~~~~~~~~~~~~~~~~
- User opts to modify an existing task.
- User selects the task earmarked for modification.
- User stipulates the attribute to be altered and provides the new value.
- The system implements the update with the new value.

3. Deleting a Task
~~~~~~~~~~~~~~~~~~~
- User elects to delete a specific task.
- User identifies the task slated for deletion.
- The system effectuates the removal of the designated task from the todo list.

4. Viewing the Todo List
~~~~~~~~~~~~~~~~~~~~~~~~~
- User selects the option to peruse the todo list.
- The system presents pending and completed tasks distinctly.

Constraints
========================
- The application is confined to managing tasks within a single session and lacks support for user authentication or persistent storage of tasks.
- Due dates must conform to a specified format (e.g., DD.MM) to ensure accurate processing by the application.

Assumptions
========================
- Users possess a rudimentary understanding of navigating menu-driven interfaces.
- Users comprehend the fundamentals of task management and can furnish pertinent task details.
