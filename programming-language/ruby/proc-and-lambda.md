# Proc and Lambda

Proc and lambda are both closures in Ruby, which can be used for deferred evaluation ("lazy evaluation").

Using `Proc.new`:

```ruby
inc = Proc.new { |x| x + 1 }
inc.call(42) # => 43
```

Using `lambda`:

```ruby
inc = lambda { |x| x + 1 }
inc.call(42)
```

It can also be written simply as follows:

```ruby
inc = -> x { x + 1 }
```

There are two main differences between `proc` and `lambda`.

The first one is the `return` behavior. Because procs are designed to work within other Ruby control structures, using `return` keyword in procs will return from the control structure. Look at the following example:

```ruby
def increment
  p = Proc.new { return 42 }
  result = p.call
  return result + 1 # will not be executed
end

increment # => 42
```

To avoid the problem we should not use the `return` keyword for procs.

The other difference is `proc` will ignore redundant arguments, or assign `nil` values to lacking arguments, while `lambda` is strict with the number of arguments.
