class MusicLibrary:
    def __init__(self):
        self.library_ = []

    def add(self, track):
        self.library_.append(track)

    def search(self, keyword):
        relevant_tracks = []
        for track in self.library_:
            if keyword.lower() in track.title.lower() or keyword.lower() in track.artist.lower():
                relevant_tracks.append(track)
        return relevant_tracks
