
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# def test_shows_correct_task():
#     reminder = Reminder("Kay")
#     result = reminder.remind_me_to("Walk the dog")
#     assert result == "Walk the dog"
#     Doesn't work because it doesn't return anything using that method
    
#     The reason you're encountering the error `AssertionError: assert None == 'Walk the dog'` is because your method `remind_me_to()` in the `Reminder` class doesn't return anything, so it implicitly returns `None`. Therefore, when you're assigning the result of `reminder.remind_me_to("Walk the dog")` to `result`, it's `None`, not the task itself.

# To fix this, you can modify the `remind_me_to()` method to return the task. Here's the updated code:

# ```python
# class Reminder:
#     def __init__(self, name):
#         self.name = name

#     def remind_me_to(self, task):
#         self.task = task
#         return self.task

#     def remind(self):
#         return f"{self.task}, {self.name}!"
# ```

# Now, when you run the test, it should pass without errors.
    
def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Jeli")
    reminder.remind_me_to("  Eat the lunch")
    result = reminder.remind()
    assert result == "  Eat the lunch, Jeli!"

# Various other tests from CHATGPT
    

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

def test_remind_method_with_different_task():
    reminder = Reminder("John")
    reminder.remind_me_to("Buy groceries")
    result = reminder.remind()
    assert result == "Buy groceries, John!"

def test_remind_method_after_changing_task():
    reminder = Reminder("Bob")
    reminder.remind_me_to("Do homework")
    reminder.remind_me_to("Go to the gym")  # Changing the task
    result = reminder.remind()
    assert result == "Go to the gym, Bob!"

def test_name_attribute():
    reminder = Reminder("Jane")
    assert reminder.name == "Jane"

def test_task_attribute():
    reminder = Reminder("Michael")
    reminder.remind_me_to("Clean the house")
    assert reminder.task == "Clean the house"



