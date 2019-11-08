# Common `jcmd` Use

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
