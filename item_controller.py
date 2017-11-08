from model_todo_item import ToDoItem
from view import View

class ItemController():

    def create_item(self):
        item_name = View.user_input('Type item name: ')
        item_description = View.user_input('\nType short description (max 150 characters):')
        try:
            return ToDoItem(item_name, item_description)
        except AttributeError:
            View.display_wrong_input()