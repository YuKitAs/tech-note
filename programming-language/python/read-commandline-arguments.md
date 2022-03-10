# Read Command-line Arguments

## `sys`

With the `sys` module, a list of command line arguments can be read by position. The first argument is the name of the script itself.

```python
import sys

print sys.argv[1]
```

## `argparse`

With the help of the build-in [`argparse`](https://docs.python.org/3/howto/argparse.html) module, a Python3 script can read command-line arguments like:

```console
$ script.py <number> -f <foo-value> [-b <bar-value>]
```

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
parser.add_argument('-f', '--foo', required=True)
parser.add_argument('-b', '--bar', default='')
```

The arguments starting with `-` are optional by default. They can be simply parsed with:

```python
args = parser.parse_args()
number = args.number
foo = args.foo
```

Boolean arguments:

```python
parser.add_argument('--dryrun', action='store_true', default=False)
```
