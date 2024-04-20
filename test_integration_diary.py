from lib.secret_diary import *
from lib.diary import *
import pytest

def test_initialise_content_then_read():
    diary1 = Diary("Hello Jels, it's a new day")
    secret = SecretDiary(diary1)
    with pytest.raises(Exception) as e:
        secret.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_initialise_content_then_read_unlocked():
    diary1 = Diary("Hello Jels, it's a new day")
    secret = SecretDiary(diary1)
    secret.unlock()
    assert secret.read() == diary1.contents 

def test_initialise_content_then_lock_then_read_unlocked():
    diary1 = Diary("Hello Jels, it's a new day")
    secret = SecretDiary(diary1)
    secret.unlock()
    secret.lock()
    with pytest.raises(Exception) as e:
        secret.read()
    error_message = str(e.value)
    assert error_message == "Go away!"