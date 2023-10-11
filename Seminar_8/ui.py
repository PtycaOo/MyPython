from delete_data import delete_row
from add_data import add_row
from change_data import chenge_data

def answer_for_user():
    pass

def start_menu():
    command = int(input("Добрый день\n"
                        "Выберите функцию:\n "
                        "1. Добавить\n"
                        "2. Удалить\n"
                        "3. Изменить\n"
                        "4. Выход\n"
                        "5. Выход"))
    while command <1 or command > 5:
        command = int(input("Добрый день\n"
                        "Выберите функцию:\n "
                        "1. Добавить\n"
                        "2. Удалить\n"
                        "3. Изменить\n"
                        "4. Выход\n"
                        "5. Выход"))
    
    while command !=5:
        if command == 1:
            pass
        elif command == 2:
            pass
        elif command == 3:
            pass
        elif command == 4:
            pass
        elif command == 5:
            pass
