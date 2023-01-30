
import view
import model

def start():
    
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()

        match user_choice:

            case 1:
                phone_book = model.get_phone_book()
                view.show_contact(phone_book)
                
            case 2:
                model.open_phone_book()
                                
            case 3:
                model.save_phone_book()
                view.save_success()
                
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
                               
            case 5:
                pass
            
            case 6:
                index = view.del_item()
                model.delete(index)
            
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contact(result)
                
            
            
                