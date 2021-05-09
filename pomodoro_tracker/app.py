import logging
import typing as t
from unittest.mock import MagicMock

from pomodoro_tracker.track import Tracker
from pomodoro_tracker.utils import find


def run_tracker(*args: t.Any) -> None:
    '''
    Wrapper for Tracker.start infinite loop. Parse CLI arguments.
    '''

    try:

        tracker = Tracker()

        if '--no-save' in args:

            tracker.writer.file = MagicMock()

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

            tracker.writer.folder = folder

        if find('--extension', args):

            ext: str = find('--extension', args).split('=')[-1].strip()

            tracker.writer.set_extension(ext)

        # Here we actually start infinite loop with user's input

        tracker.start()

    except Exception as e:
        logging.exception(e, exc_info=True)

    except KeyboardInterrupt:
        ...

    finally:
        tracker.stop()
