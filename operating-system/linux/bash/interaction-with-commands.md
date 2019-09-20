# Interaction with Commands

## Event Designators

An event designator is a reference relatively to a command line entry in the Bash history list.

`!!`: execute the last command, it's equivalent to `Up` + `Enter`.

`!<string>`: execute last command starting with specific string.

## Clear Commands

`Ctrl` + `U`: clear the current command line if the cursor is at the end

`Ctrl` + `K`: clear the current command line if the cursor is at the beginning

`Ctrl` + `W`: clear the argument before the cursor in the command line

`Ctrl` + `Y`: restore the last cleared command line

`history -c`: clear the history list
