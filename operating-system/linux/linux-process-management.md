# Linux Process Management

* `ps aux`: list current active processes with PIDs, `a` = for all users, `u` = process's owner (user), `x` = show processes not attached to a terminal (also including services like crond)

* `Ctrl` + `Z`: suspend the currently foregrounded process, which can be resumed with command `fg %1`

* `jobs`: list all the processes that the current shell is managing with job numbers

* `bg <%JOB_NUMBER>`: bring a certain or the most recently suspended process to the background, or alternative `<%JOB_NUMBER> &`

* `fg <%JOB_NUMBER>`: bring a certain or the most recently suspended process to the foreground

* `Ctrl` + `C`: terminate the currently foregrounded process by sending a `SIGINT` signal to the process

* `kill <signal> <PID>`: terminate a certain process by sending a signal (`SIGHUP`, `SIGKILL`, `SIGTERM`) which can not be ignored by the process

* `top`: a default task (process) management program for monitoring processes and system resource usage

* `htop`: a powerful interactive process viewer which is similar to `top`, can be installed with `sudo apt install htop`
