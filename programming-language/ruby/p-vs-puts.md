# `p` vs. `puts`

`p var` prints `var.inspect` and `puts` prints `var.to_s` if `var` has `to_s` method.

For example, `a = %i[a b c]` is an array of symbols, `p a` will print

```
[:a, :b, :c]
```

and `puts a` will print

```
a
b
c
```
