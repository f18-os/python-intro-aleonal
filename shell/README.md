TO RUN:

1. In bash, travel to the directory where shell.py lies. 
2. Type "chmod +x shell.py" to make the shell executable.
3. Execute by typing "./shell.py"

NOTES:

1. This shell can do both I/O redirections in a single command. However, it cannot do piping AND I/O in the same command.
2. This shell sets the os.environ['PS1'] value to "$: ", regardless of it was set beforehand or not. I was not able to figure out how to inherit the value set beforehand, as the "if" statement to determine that threw an error.
