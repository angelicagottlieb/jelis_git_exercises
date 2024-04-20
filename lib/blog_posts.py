class BlogPost:
    def __init__(self, id, title):
        self.id = id
        self.title = title
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"BlogPost({self.id}, {self.title})"
    