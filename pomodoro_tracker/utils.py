import typing as t

from datetime import timedelta, datetime


def form(dt: datetime, fmt: t.Optional[str] = None) -> str:
    '''
    Format datetime to string.
    '''
    return dt.strftime(fmt or '%H:%M:%S')


def pretty(td: timedelta, /) -> str:
    '''
    Format timedelta to datetime and
    Then return result of the form function.
    '''
    return form(datetime(1, 1, 1) + td)


def find(substring: str, sequence: t.Sequence[str]) -> t.Optional[str]:
    '''
    Return first element that contains the substring.
    '''

    for elem in sequence:
        if substring in elem:
            return elem
    return None
