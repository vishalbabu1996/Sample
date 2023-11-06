class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task.description} (Due: {task.due_date}, Priority: {task.priority})")

        print("\nCompleted Tasks:")
        for i, task in enumerate(self.completed_tasks):
            print(f"{i+1}. {task.description}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = True
            self.completed_tasks.append(task)
            del self.tasks[task_index]

    def update_task(self, task_index, description, due_date, priority):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.description = description
            task.due_date = due_date
            task.priority = priority

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.complete_task(task_index)

        elif choice == '4':
            task_index = int(input("Enter task index to update: ")) - 1
            description = input("Enter new description: ")
            due_date = input("Enter new due date: ")
            priority = input("Enter new priority: ")
            todo_list.update_task(task_index, description, due_date, priority)

        elif choice == '5':
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
