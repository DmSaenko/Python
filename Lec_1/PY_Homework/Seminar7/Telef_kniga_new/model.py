

phone_book = []

path = 'phone_book.txt'

def get_phone_book():
    
    global phone_book
    return phone_book


def open_phone_book():
    
    global phone_book
    global path
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = data.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))
            
def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)
            
def save_phone_book():
    
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, w, encoding = 'UTF-8') as file:
        data = data.write('\n'.join(data))
        
def search_contact(search: str):
    
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
        return search_results
                 