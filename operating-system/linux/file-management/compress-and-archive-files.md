# Compress and Archive Files

## `tar`

The `tar` (tape archiver) command is used to package files into a single archive file (`.tar`) called tarball. By adding the option `-z` the tarball can be compressed to `.tar.gz` using `gzip` (with `g` referring to GNU). All files in the tarball are compressed together, which can result in faster compression and smaller file sizes. However, the files cannot be accessed individually without fully decompressing the tarball.

### Create a tarball

With `-c` for **create** and `-f` for **file**:

```console
$ tar -cf <file.tar> <directory>
```

### Create a compressed tarball

With `-z` for **gzip**:

```console
$ tar -czf <file.tar.gz> <directory>
```

### List all the files in a tarball

With `-t` or `--list`:

```console
$ tar -tf <file.tar>
```

### Extract files to a directory

With `-x` for **extract**:

```console
$ tar -xf <file.tar> <directory>
```

### Decompress tarball and extract files

```console
$ tar -xzf <file.tar.gz> <directory>
```

The `-v` option can be added for verbose output.

## `zip`

The `zip` command is used to compress files individually and then bundle them into an archive (`.zip`). It allows individual files to be accessed directly without decompressing the entire archive.

### Compress and package

With `-r` for **recursive**:

```console
$ zip -r <file.zip> <directory>
```

### Extract and decompress zipped archive

```console
$ unzip <file.zip>
```
