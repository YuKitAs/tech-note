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

## `jps`

`jps` is command to check all the running JVM processes. By default it will list the PID and the simple name of the main class or the name of the running executable, like:

```
26929 some-project.jar
24595 Main
26997 Jps
```
