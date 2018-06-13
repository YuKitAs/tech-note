# `su -` and `su root`

There was a time that I didn't realize the real difference between `su -` and `su root`, because they both required the password for `root` and the environments looked similar. Howerver, I almost forgot the fact that `su <username>` only switches to the user, while `su - <username>` invokes a login shell after switching the user, with cleared environment (except for a few variables).

For example, we are now in some directory with username `yukitas`:

```console
yukitas@my-pc:~/my-dir$
```

Using `su - root` we will be at the home directory of the `root` with a `root` environment:

```console
root@my-pc:~#
```

But using `su root` we will still be in the same directory, but just looks like being `root`:

```console
root@my-pc:/home/yukitas/my-dir#
```

When a `root` account is enabled with a password, `su - root` can be shortened to `su -` and `su root` to `su`. When there is no root password on some default installation, invoking `su` may fail (it's OS-dependent).
