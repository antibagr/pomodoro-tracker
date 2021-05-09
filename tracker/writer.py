import os
import _io
import typing as t
from datetime import date

from utils import form


class BaseFileWriter:

    file_extension: str

    def __init__(self, file_extension: t.Optional[str] = 'txt'):

        self._date = date.today()
        self._date_str = form(self._date, "%d-%m-%Y")
        self.file_extension = file_extension
        self._filename = f'{self._date_str}.{self.file_extension}'

        self._file: _io.TextIOWrapper = None

    @property
    def file(self) -> _io.TextIOWrapper:

        if self._file is None:
            self._file = open(self._filename, 'a')

        return self._file

    def write(self, line: t.AnyStr) -> None:

        line = f'{line}\n'

        self.file.write(line)

    def close(self) -> None:

        if self.file and not self.file.closed:
            self.file.close()


class FileWriter(BaseFileWriter):

    def start_line(self) -> None:
        '''
        Write start line if file is empty.
        '''

        if os.stat(self._filename).st_size == 0:
            self.write(f'Start tracker at {form(datetime.now())}')
