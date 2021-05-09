# Pomadoro Tracker

CLI tools for [pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)

### Installation

Install package with pip:

`pip install rudie-pomodoro-tracker==0.1.0`

After it you can launch CLI with simply:

`pomodoro`

### Avaiable customization:

| Flag | Action |
| --- | --- |
| --no-save | Do not **store** sessions to file |
| --no-clear | Do not clear output after creating session |
| --folder=new | Use specific folder for storing sessions. Defaults to *daily* |
| --extension=txt | Use specific files' extension. Defaults to *.pomodoro* |

### Example:

`pomodoro --folder=project_1 --extension=log`

By default all pomodoro logs stored in folder called *daily* where you run `pomodoro` command.
Files have extension .pomodoro, but they are simply text files.

You can change both folder name and extension flags using corresponding cli flags.


Then use input to manage sessions:

lap or l      - make new lap
end or e      - exit
anything else - lap title
