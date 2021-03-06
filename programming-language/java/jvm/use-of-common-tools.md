# Use of Common Tools

## `jcmd`

`jcmd` is a utility to send diagnostic commands to the running JVM.

* List all the running Java processes:

  ```console
  $ jcmd -l
  ```

* Check JVM version:

  ```console
  $ jcmd <pid|main class> VM.version
  ```

* Check JVM system properties:

  ```console
  $ jcmd <pid|main class> VM.system_properties
  ```

* Check JVM flags:

  ```console
  $ jcmd <pid|main class> VM.flags
  ```

* Print threads with stack traces:

  ```console
  $ jcmd <pid|main class> Thread.print
  ```

* Create a heap dump:

  ```console
  $ jcmd <pid> GC.heap_dump </path/to/file>
  ```

  If not specifying an absolute path, the dump file will be generated in the directory of the application.


## `jconsole`

`jconsole` is a graphical profiling tool for monitoring and managing a local or remote JVM.


## `jps`

`jps` is a command to check all the instrumented JVM process status. By default it will list the PID and the simple name of the main class or the name of the running executable on the local machine like:

```console
$ jps
26929 some-project.jar
24595 Main
26997 Jps
```

This is an experimental tool. With the PID we can use other (experimental) tools like `jinfo`, `jmap` and `jstack` for troubleshooting.

## Reference

* [JDK Tools and Utilities](https://docs.oracle.com/javase/8/docs/technotes/tools/), Oracle Java Documentation
