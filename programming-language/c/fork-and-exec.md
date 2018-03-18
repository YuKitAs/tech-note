# Fork and Exec

When we use a shell to run an external program in the background, the shell need the `fork()` system call to get a new process running and the `exec()` system call (or other variants) to replace the current process with the external program.

The following example shows how to use `fork()` and `exec()`. The `execute()` function returns either an error code or the exit status of the child:

```c
int execute(char **argv) {
  int child_pid;
  int status;

  if (child_pid < 0) {
    // forking child process failed
    return ERROR_CODE;
  } else if (child_pid == 0) {
    // in child
    execvp(*argv, argv);
    // this line will only be reached when exec failed
    exit(ERROR_CODE);
  } else {
    /* the parent waits for child process until it terminates */

    if (waitpid(child_pid, &status, 0) == -1) {
      return ERROR_CODE;
    }

    if (WIFEXITED(status)) {
      // the child terminated normally
      return WEXITSTATUS(status);
    } else {
      return ERROR_CODE;
    }
  }
}
```

## Reference

* [exec(3)](https://linux.die.net/man/3/exec) - Linux man page
* [waitpid(2)](https://linux.die.net/man/2/waitpid) - Linux man page
