tasks = []
def showOperations():
   print("\nWelcome to your Todo App!")
   print("What would you like to do?")
   print(" 1 • CREATE a new task ")
   print(" 2 • READ any existing task ")
   print(" 3 • UPDATE any  task ")
   print(" 4 • DELETE existing task ")
   print(" 5 • TERMINATE program ")

def createTask():
   task=input("Enter the task you want to add: ") 
   tasks.append(task)  
   print("Great! task  Added to your to-dos 💪")
            
def readTask():
    if not tasks:
        print("You don't have any tasks yet. Add your first task to get started!")
    else:
        print(f"You have {len(tasks)} tasks to complete:")
    for i,task in enumerate(tasks, start=1):
        print(f" Task {i}: {task}")

def updateTask():
    readTask()
    num = input("Which task would you you like to update? (Enter task number): ")
    if num.isdigit():
        num=int(num)
        if 1<=num <=len(tasks):
            new_task=input("Enter the updated task: ")
            tasks[num-1]=new_task
            print("✓ Task updated successfully!")
        else:
            print("Oops! That task number doesn't exist.")
    else:
        print("Please enter a valid task number.")

def deleteTask():
    readTask()
    num=input("Which task would you like to delete? (Enter number): ")
    if num.isdigit():
        num=int(num)
        if 1<=num <=len(tasks):
            deleted=tasks.pop(num-1)
            print(f"✓ '{deleted}' has been successfully removed!")
        else:
            print("Oops! That task number doesn't exist.")
    else:
        print("Please enter a valid number.")           

while True:
    showOperations()
    choose=input("\nWhat would you like to do? (1-5): ")  

    if choose=="1":
        createTask()
    elif choose=="2":
        readTask()
    elif choose=="3":
        updateTask()
    elif choose=="4":
        deleteTask()
    elif choose=="5":
        print("\nThank you for using Todo App! Have a productive day! 👋")
        break
    else:
        print("Oops! Please choose a number between 1 and 5.") 
