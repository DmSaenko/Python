

def main_menu():
    commands = ['Показать все контакты', 
                'Открыть файл', 
                'Сохранить файл', 
                'Новый контакт', 
                'Изменить контакт', 
                'Удалить контакт', 
                'Найти контакт', 
                'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t {i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contact(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
            
    else:
        print('Телефонная книга пуста или не загружена')
        
            
def load_success():
    print('Телефонная книга загружена успешно')
    
def save_success():
    print('Телефонная книга сохранена успешно')
    
def new_contact():
    name = input('Введите Имя и Фамилию контакта: ')
    phone = input('Введите # Телефона контакта: ')
    comment = input('Введите комментарий: ')
    
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search


def making_changes() -> bool:
    while True:
        user_res = input('У вас есть не сохраненный результат, сохранить? (Y/n)').lower().strip()
        if user_res == 'y' or user_res == 'n':
            if user_res == 'y':
                user_res = True
                return user_res
            else:
                user_res = False
                return user_res
        else:
            print('Введите только "Y" или "N"!')
            
            
def del_item(meaning: list):
    meaning = []
    while True:
        try:
            x = int(input('Введите "ID" контакта: '))
            for i in range(0, len(meaning), 2):
                if x == int(meaning[i]):
                    return x
            else:
                print('Укажите доступный ID: \n')
        except:
            print('Только число!\n')
    
    
