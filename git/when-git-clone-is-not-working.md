# When `git clone` is not working

When I use Gitbash and try to copy the web URL of a Git repo to the terminal after `git clone`, sometimes I would get an error message like:

```console
$ fatal: I don't handle protocol 'git clone https'
```

Most possibly it's because the space between `git clone` and the URL is actually an invisible special character. So just delete it and type the space manually it should work.
