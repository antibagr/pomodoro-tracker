import os
import typing as t
from datetime import date, datetime

import _io

from pomodoro_tracker.utils import form


class BaseFileWriter:
    '''
    File buffer wrapper, keeps buffer opened,
    until close() method called explicitly.

    Create folder to store file when you first
    try to access it (e.g. using write() method)

    If you need to set different extension,
    folder and whatnot, please do it
    before Tracker.start() called.

    '''

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
        '''
        Set new file extension. Update filename.
        '''

        self.file_extension = file_extension
        self._filename = f'{self._date_str}.{self.file_extension}'

    @property
    def folder(self) -> str: return self._folder

    @folder.setter
    def folder(self, folder_name: str) -> None:
        '''
        Set new folder to store file.
        '''

        self.folder_name = folder_name
        self._folder = os.path.join(os.getcwd(), self.folder_name)

    @property
    def file(self) -> _io.TextIOWrapper:
        '''
        Create folder to store sessions.
        Compile filename and open buffer.

        Returns:
            _io.TextIOWrapper: opened buffer

        '''

        if self._file is None:

            if not os.path.exists(self._folder):
                os.mkdir(self._folder)

            self._file = open(os.path.join(self._folder, self._filename), 'a')

        return self._file

    @file.setter
    def file(self, file: t.Any) -> None:
        '''
        You can set your own buffer.
        Used to mock file with --no-save option.
        '''
        self._file = file

    def write(self, line: t.AnyStr) -> None:
        '''
        Write new line.
        '''

        line = str(line) + '\n'

        self.file.write(line)

    def close(self) -> None:
        '''
        Close opened buffer.
        '''

        if self.file and not self.file.closed:
            self.file.close()


class FileWriter(BaseFileWriter):

    def start_line(self) -> None:
        '''
        Write start line with tracker start time if file is empty.
        '''

        if os.path.exists(self._filename) and os.stat(self._filename).st_size != 0:
            return

        self.write(f'Start tracker at {form(datetime.now())}\n')
