from lib.secret_diary import *
from unittest.mock import Mock
import pytest

def test_starts_off_raising_exception_if_trying_to_read():
    fake_diary = Mock()
    fake_diary.contents = "Hello"
    secret = SecretDiary(fake_diary)
    with pytest.raises(Exception) as e:
        secret.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_returns_contents_if_unlocked():
    fake_diary = Mock()
    fake_diary.read.return_value = "Hello Jels"
    secret = SecretDiary(fake_diary)
    secret.unlock()
    assert secret.read() == "Hello Jels"

def test_raises_exception_with_double_lock():
    fake_diary = Mock()
    fake_diary.contents = "Hello"
    secret = SecretDiary(fake_diary)
    secret.lock()
    with pytest.raises(Exception) as e:
        secret.read()
    error_message = str(e.value)
    assert error_message == "Go away!"


def test_for_attribute_of_lock():
    fake_diary = Mock()
    fake_diary.contents = "Hello"
    secret = SecretDiary(fake_diary)
    assert secret.locked == True 


def test_for_attribute_of_lock_unlocked():
    fake_diary = Mock()
    fake_diary.contents = "Hello"
    secret = SecretDiary(fake_diary)
    secret.unlock()
    assert secret.locked == False 
