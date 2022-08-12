# Link Local Packages

If Node Project A is using B as dependency and we want to test local changes of B in A, we can use `yarn link`.

In Project B run:

```console
$ yarn build
$ cd dist
$ yarn link
```

Then in Project A:

```console
$ yarn link <package-B>
```

The links are registered in `~/.config/yarn/link` by default.

To reverse the link, run `yarn unlink <package>` in Project A.
