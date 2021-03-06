# Accumulator in Ruby

`reduce`(alias `inject`) is an enumerable method in Ruby. It's used to iterate over a collection applying an operation specified by a block or a symbol, and return the accumulator.

The following are equivalent examples to sum up 1 to 10:

```ruby
(1..10).reduce(:+) # => 55
(1..10).reduce(0, :+) # => 55
(1..10).inject { |sum, n| sum + n } # => 55
(1..10).inject(0) { |sum, n| sum + n } # => 55
```

As is shown, if we don't specify an initial value explicitly, the first element of collection will be used as the initial value.

We can iterate over an array and select elements by a given condition. In the following example, a block is passed on each accumulator value with an empty array as the initial value:

```ruby
players = [{ name: "foo", level: 6 }, { name: "bar", level: 11 }, { name: "baz", level: 8 }, { name: "qux", level: 12 }]

players.reduce([]) do |names, player|
  names << player[:name] if player[:level] >= 10
  names
end
# => ["bar", "qux"]
```

It's equivalent to:

```ruby
names = []
players.each do |player|
  names << player[:name] if player[:level] >= 10
end

names
# => ["bar", "qux"]
```

More efficient than using `select` and `map` which would loop over the array twice:

```ruby
players.select { |player| player[:level] >= 10 }.map { |player| player[:name] } # => ["bar", "qux"]
```
