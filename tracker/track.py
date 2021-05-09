import typing as t
from datetime import date, datetime, timedelta

from console import ConsolePrinter
from display import TYPES
from session import Session
from writer import FileWriter

from utils import pretty


class Tracker:

    _is_work_session: bool

    sessions: t.List[Session]

    def __init__(self) -> None:

        self._is_work_session: bool = True

        self.sessions = []

        self.writer = FileWriter()
        self.console = ConsolePrinter()

    def count_total(self) -> t.Dict[str, timedelta]:

        totals: t.Dict[str, timedelta] = {}

        for session in self.sessions:

            if session.title not in (TYPES.WORK, TYPES.RELAX):
                continue

            if session.title in totals:
                totals[session.title] += session.duration
            else:
                totals[session.title] = session.duration

        return totals

    def print_total(self) -> None:

        total = ", ".join([f"{k} : {pretty(v)}" for k,
                           v in self.count_total().items()])

        total = f'\n{total}\n'

        self.console.print(total)

        self.writer.write(total)

    def start(self) -> None:

        session_start = datetime.now()

        self.writer.start_line()

        while True:

            self.console.display(self.sessions)

            inp: str = input(': ')

            now = datetime.now()

            if inp in ('end', 'end!', 'e', 'e!'):

                self.console.display(self.sessions)

                if '!' not in inp:
                    self.print_total()

                raise KeyboardInterrupt()

            if inp in ('lap', 'l'):

                title = TYPES.WORK if self._is_work_session else TYPES.RELAX

                self._is_work_session = not self._is_work_session

            elif inp and len(inp) < 20:
                title = inp
            else:
                continue

            session = Session(title, session_start, now)

            self.sessions.append(session)

            self.writer.write(str(session))

            session_start = now

    def stop(self) -> None:
        '''
        Close tracker, close file buffer.
        '''
        self.writer.close()
