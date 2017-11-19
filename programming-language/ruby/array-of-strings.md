# Array of Strings

In Ruby, `%w[foo bar baz qux]` and `%W[foo bar baz qux]` are shortcuts for an array of String `['foo', 'bar', 'baz', 'qux']` without using quotes and commas.

The difference between `%w` and `%W` is that `%W` supports `\n` (line break) like in double quotes. For example, `puts %w[foo\n bar]` will output

```
foo\n
bar
```

And `puts %W[foo\n bar]` will output

```
foo
bar
```

More reference: General Delimited Input, [Ruby Docs](http://ruby-doc.com/docs/ProgrammingRuby/)
