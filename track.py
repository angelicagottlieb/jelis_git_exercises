class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        if keyword.lower() == self.title.lower() or keyword.lower()== self.artist.lower():
            return True
        else:
            return False 


