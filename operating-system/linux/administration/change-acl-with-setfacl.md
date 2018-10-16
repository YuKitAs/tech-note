# Change ACL with `setfacl`

`setfacl` is used to change ACL (Access Control Lists) of files and directories. Compared to `chmod`, `setfacl` can grand permissions to specific users and groups.

For example, grand user `yukitas` with read and write access to `file` (`-m` for modify):

```console
$ setfacl -m u:yukitas:rx file
```
