class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 

    def count_words(self):
        return len(self.contents.split())
    
    def extract_number(self):
        numbers = []
        current_number = ""
        for char in self.contents:
            if char.isdigit():
                current_number = current_number + char
                if len(current_number) == 11:
                    numbers.append(current_number)
                    current_number = ""
            else:
                current_number = ""
        if len(current_number) == 11:
            numbers.append(current_number)
        return numbers 
# can i do this in a way where I don't create a list or I don't return anything?
