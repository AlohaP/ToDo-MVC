from view import View
from item_controller import ItemController

class HandleController():

    def __init__(self, todo_handle):
        self.todo_handle = todo_handle
        self.item_controller = ItemController

    def show_all_items(self):
        item_list = list(self.todo_handle.get_item_list())
        for i in range(len(item_list)):
            item_list[i] = str(item_list[i])
        View.display_items(item_list)

    def remove_item(self, index):
        try:
            self.todo_handle.remove_item(index)
            View.display_item_delete()
        except IndexError:
            View.display_wrong_input()
        except ValueError:
            View.display_wrong_input()

    def add_item(self, item):
        self.todo_handle.add_item(item)

    def mark_item(self, index):
        try:
            self.todo_handle.mark_item(index)
            View.display_item_mark()
        except IndexError:
            View.display_wrong_input()
        except ValueError:
            View.display_wrong_input()

    def display_item(self, index):
        try:
            View.display_detailed_item(self.todo_handle.display_item(index))
        except IndexError:
            View.display_wrong_input()
        except ValueError:
            View.display_wrong_input()

    def modify_item(self, index, new_item):

        try:
            self.todo_handle.modify_item(index, new_item)
        except IndexError:
            View.display_wrong_input()
        except ValueError:
            View.display_wrong_input()