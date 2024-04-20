# #Unit tests using mocking!
from unittest.mock import Mock
from lib.music_library import *

# def test_library_adds_tracks_with_mocks():
#     library = MusicLibrary()

#     fake_track_artist_one = Mock()
#     fake_track_artist_one.add.return_value = "Toxic", "Britney Spears"

#     library.add(fake_track_artist_one)
    
#     assert library.library_ == [fake_track_artist_one]

#  Don't need to do return value if it's not returning anything!!!

def test_library_adds_tracks_with_mocks():
    library = MusicLibrary()
    fake_track_artist_one = Mock()
    fake_track_artist_one.title = "Toxic"
    fake_track_artist_one.artist = "Britney Spears"
    library.add(fake_track_artist_one)
    assert library.library_ == [fake_track_artist_one]

def test_library_adds_tracks_with_mocks_and_searches():
    library = MusicLibrary()
    fake_track_artist_one = Mock()
    fake_track_artist_two = Mock()
    fake_track_artist_one.title = "Toxic"
    fake_track_artist_one.artist = "Britney Spears"
    fake_track_artist_two.title = "Paparazzi"
    fake_track_artist_two.artist = "Lady Gaga"
    library.add(fake_track_artist_one)
    library.add(fake_track_artist_two)
    result = library.search("papa")
    assert result == [fake_track_artist_two]