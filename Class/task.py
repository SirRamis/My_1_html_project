HELP = """
help - напечатать справку по программе.  
add - добавить задачу в список ( название задачи запрошиваем у пользователя). 
show -напечатать все добавленные задачи."""
tasks = []

run = True

while run:
    command =  input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(SHOW)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print("Задача добавлена")
    else:
        print("Неизвестная команда")
        run = False

print("До свидания!")
