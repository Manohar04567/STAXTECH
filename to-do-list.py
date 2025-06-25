import sys

# Store tasks in a list of dictionaries
tasks = []

def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{i}. [{status}] {task['title']} (Priority: {task['priority']})")

def add_task():
    title = input("Enter task title: ").strip()
    priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()
    tasks.append({"title": title, "priority": priority, "completed": False})
    print("Task added successfully!")

def edit_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new title (leave blank to keep current): ").strip()
            new_priority = input("Enter new priority (Low/Medium/High, leave blank to keep current): ").strip().capitalize()

            if new_title:
                tasks[index]['title'] = new_title
            if new_priority:
                tasks[index]['priority'] = new_priority

            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
