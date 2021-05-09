import os
import typing as t
from datetime import date, datetime

import _io

from pomodoro_tracker.utils import form


class BaseFileWriter:

    file_extension: str = 'pomodoro'

    folder_name: str = 'daily'

    def __init__(self, file_extension: t.Optional[str] = None):

        self._date = date.today()
        self._date_str = form(self._date, "%d-%m-%Y")
        self.file_extension = file_extension or self.file_extension
        self._filename = f'{self._date_str}.{self.file_extension}'

        self._file: _io.TextIOWrapper = None

        self._folder = os.path.join(os.getcwd(), self.folder_name)

    def set_extension(self, file_extension: str) -> None:

        self.file_extension = file_extension
        self._filename = f'{self._date_str}.{self.file_extension}'

    def set_folder(self, folder_name: str) -> None:

        self.folder_name = folder_name
        self._folder = os.path.join(os.getcwd(), self.folder_name)

    @property
    def file(self) -> _io.TextIOWrapper:

        if self._file is None:

            if not os.path.exists(self._folder):
                os.mkdir(self._folder)

            self._file = open(os.path.join(self._folder, self._filename), 'a')

        return self._file

    def write(self, line: t.AnyStr) -> None:

        line = str(line) + '\n'

        self.file.write(line)

    def close(self) -> None:

        if self.file and not self.file.closed:
            self.file.close()


class FileWriter(BaseFileWriter):

    def start_line(self) -> None:
        '''
        Write start line if file is empty.
        '''

        if os.path.exists(self._filename) and os.stat(self._filename).st_size != 0:
            return

        self.write(f'Start tracker at {form(datetime.now())}\n')
