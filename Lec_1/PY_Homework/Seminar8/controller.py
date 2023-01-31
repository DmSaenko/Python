from model import dp
from view import d

def journal():

    num_class = d.imp_num() 
    dp.init_path(num_class) 
    dp.open() 

    file = dp.get()

    temp_key = d.inp_subject(file) 
    dp.init_subject(temp_key) 


    while True:
        temp_dict = dp.get_subject()
        d.print_class(temp_dict)
        surname = d.imp_surname(temp_dict) 
        if surname == 'Exit':
            dp.update_data()
            dp.save_data()
            break 
        score = d.inp_rating() 
        dp.update_score(surname, score) 
        