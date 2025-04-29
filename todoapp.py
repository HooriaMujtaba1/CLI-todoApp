class TodoApp:
    def __init__(self):
        self.tasks = []  # Initialize empty list of tasks

    def show_operations(self):
        print("\n📋 Welcome to your Todo App!")
        print("What would you like to do?")
        print(" 1 • CREATE a new task")
        print(" 2 • READ existing tasks")
        print(" 3 • UPDATE a task")
        print(" 4 • DELETE a task")
        print(" 5 • EXIT the app")

    def create_task(self):
        task = input("Enter the task you want to add: ")
        self.tasks.append(task)
        print("✅ Task added to your to-dos!")

    def read_tasks(self):
        if not self.tasks:
            print("📭 You don't have any tasks yet. Add your first task to get started!")
        else:
            print(f"📜 You have {len(self.tasks)} tasks to complete:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"   {i}. {task}")

    def update_task(self):
        if not self.tasks:
            print("📭 No tasks available to update!")
            return

        self.read_tasks()
        num = input("Which task would you like to update? (Enter task number): ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(self.tasks):
                new_task = input("Enter the updated task: ")
                self.tasks[num - 1] = new_task
                print("✅ Task updated successfully!")
            else:
                print("❌ That task number doesn't exist.")
        else:
            print("❌ Please enter a valid task number.")

    def delete_task(self):
        if not self.tasks:
            print("📭 No tasks available to delete!")
            return  # Immediately exit if no tasks

        self.read_tasks()
        num = input("Enter the task number you want to delete: ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(self.tasks):
                deleted = self.tasks.pop(num - 1)
                print(f"✅ '{deleted}' has been successfully removed!")
            else:
                print("❌ That task number doesn't exist.")
        else:
            print("❌ Please enter a valid number.")

    def run(self):
        while True:
            self.show_operations()
            choose = input("\nChoose an option (1-5): ")

            if choose == "1":
                self.create_task()
            elif choose == "2":
                self.read_tasks()
            elif choose == "3":
                self.update_task()
            elif choose == "4":
                self.delete_task()
            elif choose == "5":
                print("\n👋 Thank you for using Todo App! Have a productive day!")
                break
            else:
                print("❌ Please choose a number between 1 and 5.")

# Create object and start app
if __name__ == "__main__":
    app = TodoApp()
    app.run()
