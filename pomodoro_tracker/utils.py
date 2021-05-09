import typing as t

from datetime import timedelta, datetime


def form(dt: datetime, fmt: t.Optional[str] = None) -> str:
    return dt.strftime(fmt or '%H:%M:%S')


def pretty(td: timedelta, /) -> str:
    return form(datetime(1, 1, 1) + td)
