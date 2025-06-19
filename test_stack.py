import pytest
from stack import Stack


def test_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(IndexError):
        s.pop()


def test_peek_and_size():
    s = Stack()
    s.push('a')
    s.push('b')
    assert s.peek() == 'b'
    assert s.size() == 2
    s.pop()
    assert s.peek() == 'a'
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()
    with pytest.raises(IndexError):
        s.peek()
