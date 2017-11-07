class ToDoItem:

    max_name_length = 20
    max_description_length = 150

    def __init__(self, name, description):
        if len(name) > self.max_name_length or len(description) > self.max_description_length:
            raise AttributeError
        self.name = name
        self.description = description
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        return ('[{}] {} {}').format('x' if self.is_done == True else ' ', self.name, self.description)
