ABOUT = 'Time tracker application'

_cmd = [
    ('lap or l', 'make new lap'),
    ('end or e', 'exit'),
    ('anything else', 'lap title'),
]

COMMANDS: str = '\n'.join(
    [' - '.join(list(map(lambda e: f"{e:<13}", l))) for l in _cmd])


class TYPES:

    WORK = 'work session'
    RELAX = 'chill'
