# Linux Process Management

* `ps aux`: list current active processes with PIDs, `a` = for all users, `u` = process's owner (user), `x` = show processes not attached to a terminal (also including services like crond)

* `jobs`: list all the processes that the current shell is managing with job numbers

* `bg <%JOB_NUMBER>`: bring a certain or the most recently suspended process to the background, or alternative `<%JOB_NUMBER> &`, but the process will be killed when the shell session is closed.

* `fg <%JOB_NUMBER>`: bring a certain or the most recently suspended process to the foreground

* `Ctrl` + `Z`: suspend the currently foregrounded process, which can be resumed with command `fg %1`

* `Ctrl` + `C`: terminate the currently foregrounded process by sending a `SIGINT` signal to the process

* `kill <signal> <PID>`: terminate a certain process by sending a signal (`SIGHUP`, `SIGKILL`, `SIGTERM`) which can not be ignored by the process

* `nohup`: stands for no hang up, with `nohup <command> &` the process will still be running in the background even if the shell session is closed.

* `top`: a default task (process) management program for monitoring processes and system resource usage

* `htop`: a powerful interactive process viewer which is similar to `top`, can be installed with `sudo apt install htop`
