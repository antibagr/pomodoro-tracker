import logging

from track import Tracker



def run_tracker() -> None:
    '''
    Wrapper for Tracker.start infinite loop.
    '''

    try:
        tracker = Tracker()

        tracker.start()

    except Exception as e:
        logging.exception(e, exc_info=True)

    except KeyboardInterrupt:
        pass

    finally:
        tracker.stop()
