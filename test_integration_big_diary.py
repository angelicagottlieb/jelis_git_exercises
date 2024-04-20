from lib.diary import *
from lib.big_diaryentry import *
from lib.big_todo_list import *
from lib.big_todo import *

# Given a diary
# When we add two entries
# We see those entries reflected in the diary list
# """
def test_adding_two_entries():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "I ate pasta")
    entry2 = DiaryEntry("Day 2", "I ate pizza")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.all_entries()
    assert result == [entry1, entry2]

# When we add two entries of different lengths
# The one that fits the reading time, is the one we see
# """
def test_finding_most_readable_diff_lengths():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "I ate pasta and pizza in Italy")
    entry2 = DiaryEntry("Day 2", "I ate pizza")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.find_best_chunk_for_reading_time(2,2)
    assert result == entry2

# Given a diary
# When we add two entries of different lengths that can both be read
# We see the longer one
# """
def test_finding_most_readable_diff_lengths_see_longer():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "I ate pasta today")
    entry2 = DiaryEntry("Day 2", "I ate pizza")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.find_best_chunk_for_reading_time(2,3)
    assert result == entry1

def test_finding_most_readable_diff_lengths_different():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "I ate pasta and pizza in Italy")
    entry2 = DiaryEntry("Day 2", "I ate pizza")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.find_best_chunk_for_reading_time(2,5)
    assert result == entry1 


# Given a diary
# When we add two entries with numbers in
# We can then see a list of the numbers
# """
def test_given_entries_with_numbers_see_list():
    diary = Diary()
    entry1 = DiaryEntry("Numbers 1", "Sarah's number is 07493054306 and Elior's number is 07906618030")
    entry2 = DiaryEntry("Numbers 2", "I ate pizza and met Sergio. His number is 07848998586.")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.contact_list()
    assert result == ["07493054306", "07906618030", "07848998586"]

def test_given_entries_with_numbers_see_list_extra():
    diary = Diary()
    entry1 = DiaryEntry("Numbers 1", "Sarah's number is 07493054306")
    entry2 = DiaryEntry("Numbers 2", "I ate pizza and met Sergio. His number is 07848998586.")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.contact_list()
    assert result == ["07493054306", "07848998586"]

def test_to_do_list():
    to_do_list = MyToDoList()
    todo1 = TaskToDo("Walk the dog")
    todo2= TaskToDo("Eat my lunch") 
    to_do_list.add(todo1)
    to_do_list.add(todo2)
    result = to_do_list.all_my_todos()
    assert result == [todo1, todo2]