import json
import os
todo_file = "config/todo.json"
def load_tasks():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задача '{task}' добавлена!")
def show_tasks():
    tasks = load_tasks()
    if tasks:
        print("Ваши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Список задач пуст.")
def main():
    while True:
        command = input("Введите команду (add/show/exit): ")
        if command == "add":
            task = input("Введите задачу: ")
            add_task(task)
        elif command == "show":
            show_tasks()
        elif command == "exit":
            break
        else:
            print("Неизвестная команда.")
if __name__ == "__main__":
    main()