# Git Log Output

Some useful commands to adjust the output of Git logs.

* Limit the number of last entries to output:

  ```console
  $ git log -<num>
  ```

* Show modified files in every commit:

  ```console
  $ git log --stat
  ```

* Show brief commit in one line (with format `<hash> <message>`):

  ```console
  $ git log --oneline
  ```

  It would be useful to combine with the graph to achieve a clearer view:

  ```console
  $ git log --oneline --graph
  ```

* Customize the output format:

  ```console
  $ git log --pretty=format:"%h - %an, %ar : %s"
  ```

  `%h`: commit hash, `%an`: author name, `%ar`: relative author date, `%s`: subject (commit message).

* Filter with date and/or author:

  ```console
  $ git log --since="2018-01-01" --before="2018-02-01" --author='YuKitAs'
  ```
