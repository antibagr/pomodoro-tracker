import os
import platform
import typing as t

from display import ABOUT, COMMANDS
from session import Session


class BaseConsolePrinter:

    platform: str

    def __init__(self):
        self._clear_command = 'cls' if platform.system() == 'Windows' else 'clear'

    def clear(self) -> None:
        os.system(self._clear_command)

    def print(self, line: t.AnyStr) -> None:
        print(line)

    def space(self, amount: int = 1) -> None:

        for i in range(amount):
            self.print("")


class ConsolePrinter(BaseConsolePrinter):

    def display(self, sessions: t.List[Session]) -> None:
        '''
        Print app summary and sessions list.
        '''

        self.clear()

        self.print(ABOUT)

        self.space()

        self.print(COMMANDS)

        self.space()

        self.print('\n'.join([str(s) for s in sessions]))
