class View:

    @staticmethod
    def user_input(message):
        return input(message)

    @staticmethod
    def display_menu():
        print(' (1) Add ToDo item \n', '(2) Modify item\n', '(3) Delete item \n', '(4) Mark item\n',
              '(5) Display item details\n', '(6) Display item list\n', '(7) Exit'
              )

    @staticmethod
    def display_item_add():
        print('Item added')

    @staticmethod
    def display_item_delete():
        print('Item deleted')

    @staticmethod
    def display_item_mark():
        print('Item marked')

    @staticmethod
    def display_wrong_input():
        print('Wrong input')

    @staticmethod
    def display_items(item_list):
        for id, item in enumerate(item_list):
            print(id, ' ' + item)

    @staticmethod
    def display_detailed_item(item):
        print(item)

    @staticmethod
    def replace_instruction():
        print('>>>First enter new name and description then choose wich item you want to modify<<<')