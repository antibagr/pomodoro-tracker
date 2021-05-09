from datetime import date, datetime, timedelta

from pomodoro_tracker.utils import form, pretty


class Session:
    '''
    Three types of session exist:
        working session
        relax
        another with custom title

    Args:
        title (str): header of session to use in file and console.
                     used to determine whether is it work session or not.
        start_timestamp (datetime): sesison start time.
        end_timestamp (datetime): session end time.

    Attributes:
        duration (timedelta)
        title
        start_timestamp
        end_timestamp
        working (bool): whether is it a work session or not

    '''

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
