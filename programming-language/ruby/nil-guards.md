# Nil Guards

When we want to initialize a variable if it's not been defined, we may use the `if/else` statement like:

```ruby
if defined? a && a
  a
else
  a = []
end
```

In Ruby people often write it in a simpler way using so-called `Nil Guard`:

```ruby
a ||= []
```

A little pitfall is, we need to pay attention that the value of the variable is not expected to be `nil` or `false`, because in both cases the variable will be assigned.
