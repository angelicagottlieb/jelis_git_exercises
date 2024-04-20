from lib.track import *

def test_track_class_initialises_correctly():
    track1 = Track("Paparazzi", "Lady Gaga") 
    result = track1.title
    assert result == "Paparazzi"

def test_track_class_initialises_correctly_part_two():
    track1 = Track("Paparazzi", "Lady Gaga") 
    result = track1.artist
    assert result == "Lady Gaga"

def test_track_class_returns_true_or_false():
    track1 = Track("Paparazzi", "Lady Gaga") 
    result = track1.matches("what")
    assert result == False

def test_track_class_returns_true_or_false_part_two():
    track1 = Track("Paparazzi", "Lady Gaga") 
    result = track1.matches("paparazzi")
    assert result == True