
class MyToDoList:
    def __init__(self):
        self.to_do_list = []
    
    def add(self, todo):
        self.to_do_list.append(todo)
    
    def all_my_todos(self):
        return self.to_do_list
    
