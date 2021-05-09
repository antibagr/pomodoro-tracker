import logging
import typing as t
from unittest.mock import MagicMock


from pomodoro_tracker.track import Tracker


def run_tracker(*args: t.Any) -> None:
    '''
    Wrapper for Tracker.start infinite loop.
    '''

    try:

        tracker = Tracker()

        if '-s' in args:

            tracker.writer.write = MagicMock()

        if '-d' in args:

            tracker.console.clear = MagicMock()

        tracker.start()

    except Exception as e:
        logging.exception(e, exc_info=True)

    except KeyboardInterrupt:
        pass

    finally:
        tracker.stop()
