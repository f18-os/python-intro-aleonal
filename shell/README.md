TO RUN:

1. In bash, travel to the directory where shell.py lies. 
2. Type "chmod +x shell.py" to make the shell executable.
3. Execute by typing "./shell.py"

NOTES:

1. This shell can do both I/O redirections in a single command. However, it cannot do piping AND I/O in the same command. It can also only handle one pipe per command.
2. This shell sets the os.environ['PS1'] value to "$: ", regardless of it was set beforehand or not. I was not able to figure out how to inherit the value set beforehand, as the "if" statement to determine that threw an error.

BUILT IN COMMANDS:

1. "exit" to exit
2. ">" to redirect output. e.g. wc shell.py > output.txt
3. "<" to redirect input. e.g. python3 iCountWords.py < wordlist.txt > output.txt
4. "|" to pipe output from the first command to the input of the second command. e.g. wc shell.py | cat
