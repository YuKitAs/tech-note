# Change Owner of Directory

Change the owner to the current user (`$USER`) and group (`$(id -gn $USER)`) for all the files in a directory recursively (`-R`):

```console
# chown -R $USER:$(id -gn $USER) <directory>
```
