import logging
import typing as t
from unittest.mock import MagicMock

from pomodoro_tracker.track import Tracker


def run_tracker(*args: t.Any) -> None:
    '''
    Wrapper for Tracker.start infinite loop.
    '''

    def find(target: str, sequence: t.Sequence[str]) -> t.Optional[str]:

        for x in sequence:
            if target in x:
                return x
        return None

    try:

        tracker = Tracker()

        if '--no-save' in args:

            tracker.writer.write = MagicMock()

        if '--no-clear' in args:

            tracker.console.clear = MagicMock()

        if find('--folder=', args):

            folder_guide = '\n\nPlease use --folder=new_folder_name or omit to use default.'

            try:
                folder: t.Optional[str] = find('folder=', args).split('=')[-1].strip()
            except Exception as e:
                raise ValueError(
                    'Error while parsing custom folder' + folder_guide)

            if not folder:
                raise ValueError(
                    'Custom folder name not found in arguments' + folder_guide)

            tracker.writer.set_folder(folder)

        if find('--extension', args):

            ext = find('--extension', args).split('=')[-1].strip()

            tracker.writer.set_extension(ext)



        tracker.start()

    except Exception as e:
        logging.exception(e, exc_info=True)

    except KeyboardInterrupt:
        pass

    finally:
        tracker.stop()
