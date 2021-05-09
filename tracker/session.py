from datetime import date, datetime, timedelta

from utils import form, pretty


class Session:

    title: str

    start_timestamp: datetime

    end_timestamp: datetime

    duration: timedelta

    def __init__(self, title: str, start_timestamp: datetime, end_timestamp: datetime) -> None:

        self.title = title
        self.start_timestamp = start_timestamp.replace(microsecond = 0)
        self.end_timestamp = end_timestamp.replace(microsecond = 0)

        self.duration = self.end_timestamp - self.start_timestamp

    def __str__(self) -> str:
        return f"{self.title:<20} - {pretty(self.duration):<20}" \
                f"{form(self.start_timestamp, '%d.%m %H:%M:%S')}" \
                f" - {form(self.end_timestamp):<20}"

    @property
    def working(self) -> bool:
        return self.title == 'work session'
