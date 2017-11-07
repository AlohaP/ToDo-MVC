class HandleItem:

    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, index):
        self.item_list.remove(index)

    def get_item_list(self):
        return self.item_list
