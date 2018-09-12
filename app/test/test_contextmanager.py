"""
create by hanxiao on
"""

__author__ = "hanxiao"
from contextlib import contextmanager


@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')


with book_mark():
    print('钢铁',end='')
