from unittest.mock import Mock

def test_creates_a_sophisticated_mock():
    task_list = Mock()
    task = Mock() 
    task_list.list.return_value = [task]
    task_list.count.return_value = 1
    task_list.clear.return_value = "success"

    task_list.add(task)
    assert task_list.list() == [task]
    task_list.list.assert_called()
    assert task_list.count() == 1
    task_list.count.assert_called()
    assert task_list.clear() == "success"
