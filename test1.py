class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if len(task) == 0:
            print("Please add task")
        else:
            self.tasks.append(task)
        

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"Task {idx}:\n{task}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_as_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def get_task_count(self):
        return len(self.tasks)



def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = task(title, description, due_date)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
