# Linux Process Management

* `ps`: list all the processes running on the system with PIDs

* `jobs`: list all the processes that the current shell is managing with job numbers

* `Ctrl` + `Z`: suspend the currently foregrounded process, which can be resumed with command `fg %1`

* `bg <%JOB_NUMBER>`: bring a certain or the most recently suspended process to the background

* `fg <%JOB_NUMBER>`: bring a certain or the most recently suspended process to the foreground

* `Ctrl` + `C`: terminate the currently foregrounded process by sending a `SIGINT` signal to it

* `kill <PID>`: terminate a certain process by sending `SIGKILL` signal which can not be ignored by the process
