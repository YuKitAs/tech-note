# Count File Lines

In a git project, the following command can be used to output the number of lines for each file as well as the sum:

```console
$ git ls-files | xargs wc -l
```
