from item_controller import ItemController
from item_handle_controller import HandleController
from model_todo_item import ToDoItem
from model_item_handling import HandleItem
from view import View

class RootController():

    def __init__(self):
        self.item_controller = ItemController()
        self.handle_controller = HandleController(HandleItem())

    def start(self):
        while True:
            View.display_menu()
            option = View.user_input('Please pick a number for required action: ')
            if option == '1':
                new_item = self.item_controller.create_item()
                self.handle_controller.add_item(new_item)
                View.display_item_add()
            elif option == '2':
                View.replace_instruction()
                replace_item = self.item_controller.create_item()
                chose_item = View.user_input('Enter index number of item you want to replace:')
                self.handle_controller.modify_item(int(chose_item), replace_item)
            elif option == '3':
                del_item = View.user_input('Enter index number of item you want to delete')
                self.handle_controller.remove_item(int(del_item))
            elif option == '4':
                item_to_mark = View.user_input('Enter index number of item you want to mark')
                self.handle_controller.mark_item(int(item_to_mark))
            elif option == '5':
                item_to_display = View.user_input('Enter index number of item you want to details of')
                self.handle_controller.display_item(int(item_to_display))
            elif option == '6':
                self.handle_controller.show_all_items()
            elif option == '7':
                exit('Papa')
