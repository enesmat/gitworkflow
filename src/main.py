def add_task():
    task = input("Bitte geben Sie die Aufgabe ein: ")
    with open("todo_list.txt", "a") as file:
        file.write(task + "\n")
    print("Aufgabe hinzugefügt.")

def show_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Keine Aufgaben vorhanden.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("Die Datei todo_list.txt existiert nicht.")

def mark_task_done():
    show_tasks()
    try:
        task_number = int(input("Geben Sie die Nummer der Aufgabe ein, die Sie als erledigt markieren möchten: "))
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = "X " + tasks[task_number - 1]
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print("Aufgabe als erledigt markiert.")
        else:
            print("Ungültige Aufgabennummer.")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")

def delete_task():
    show_tasks()
    try:
        task_number = int(input("Geben Sie die Nummer der erledigten Aufgabe ein, die Sie löschen möchten: "))
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks) and tasks[task_number - 1].startswith("X "):
            del tasks[task_number - 1]
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print("Aufgabe gelöscht.")
        else:
            print("Ungültige Aufgabennummer oder die Aufgabe ist nicht erledigt.")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")

def main():
    while True:
        print("\nMenü:")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Beenden")
        
        choice = input("Bitte wählen Sie eine Option (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 5.")

if __name__ == "__main__":
    main()
