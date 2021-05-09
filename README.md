CLI tools for [pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)

Run with `pomodoro` command.

Avaiable flags:

| Flag | Action |
| --- | --- |
| --no-save | Do not **store** sessions to file |
| --no-clear | Do not clear output after creating session |
| --folder=new | Use specific folder for storing sessions. Defaults to *daily* |
| --extension=txt | Use specific files' extension. Defaults to *.pomodoro* |

By default all pomodoro logs stored in folder called *daily* where you run `pomodoro` command.
Files have extension .pomodoro, but they are simply text files.

You can change both folder name and extension flags using corresponding cli flags.


Then use input to manage sessions:

lap or l      - make new lap
end or e      - exit
anything else - lap title
