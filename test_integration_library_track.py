from lib.music_library import *
from lib.track import *

def test_adding_track_and_searching():
    library = MusicLibrary()
    track1 = Track("Toxic", "Britney Spears")
    library.add(track1)
    result = library.search("spears")
    assert result == [track1]

def test_adding_two_tracks_and_searching():
    library = MusicLibrary()
    track1 = Track("Toxic", "Britney Spears")
    track2 = Track("Paparazzi", "Lady Gaga")
    library.add(track1)
    library.add(track2)
    result = library.search("papa")
    assert result == [track2]

def test_checking_list_after_add():
    library = MusicLibrary()
    track1 = Track("Toxic", "Britney Spears")
    track2 = Track("Paparazzi", "Lady Gaga")
    library.add(track1)
    library.add(track2)
    result = library.library_
    assert result == [track1, track2]

