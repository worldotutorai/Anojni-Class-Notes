# creating todo list usings oopss concetps
from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, title, description,date,time,status='pending'):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def display(self):
        pass

    def update_status(self, new_status):
        self.status = new_status

    def mark_as_completed(self):
        self.status = "Completed"
        self.display()

    def get_status(self):
        return self.status
    

# personal task
class PersonalTask(Task):
    def display(self):
        print(f"Personal Task: {self.title}\nDescription: {self.description}\nDate: {self.date}\nTime: {self.time}\nStatus: {self.status}")


# work task
class WorkTask(Task):
    def display(self):
        print(f"Work Task: {self.title}\nDescription: {self.description}\nDate: {self.date}\nTime: {self.time}\nStatus: {self.status}")


class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the todo list.")
            return  
        for task in self.tasks:
            task.display()
            print("-" * 20)
    
    def complete_task(self, task):
        if task in self.tasks:
            task.mark_as_completed()

# todo=TodoList()
# while True:
#     print("\nTODO List")
#     print("1. Add Personal Task")
#     print("2. Add Work Task")   
#     print("3. Display Tasks")
#     print("4. Mark Task as Completed")
#     print("5.Remove Task")
#     print("6. Exit")
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         title = input("Enter task title: ")
#         description = input("Enter task description: ")
#         date = input("Enter task date (YYYY-MM-DD): ")
#         time = input("Enter task time (HH:MM): ")
#         personal_task = PersonalTask(title, description, date, time)
#         todo.add_task(personal_task)
#     elif choice == '2':
#         title = input("Enter task title: ")
#         description = input("Enter task description: ")
#         date = input("Enter task date (YYYY-MM-DD): ")
#         time = input("Enter task time (HH:MM): ")
#         work_task = WorkTask(title, description, date, time)
#         todo.add_task(work_task)
#     elif choice == '3':
#         todo.display_tasks()
#     elif choice == '4':
#         title = input("Enter the title of the task to mark as completed: ")
#         for task in todo.tasks:
#             if task.title == title:
#                 todo.complete_task(task)
#                 break
#         else:
#             print("Task not found.")
#     elif choice == '5':
#         title = input("Enter the title of the task to remove: ")
#         for task in todo.tasks:
#             if task.title == title:
#                 todo.remove_task(task)
#                 print("Task removed.")
#                 break
#         else:
#             print("Task not found.")
#     elif choice == '6':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")