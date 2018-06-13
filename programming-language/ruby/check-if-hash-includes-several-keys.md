# Check if Hash Includes Several Keys

There are different methods in Ruby that can be used to check if a hash contains a certain key. For example:

```ruby
h = {a: 0, b: 1, c: 2}
h.include?(:a) # => true
h.key?(:b) # => true
h.has_key?(:c) # => true
h.member?(:d) # => false
```

How about checking several keys at one time if we don't want to write something like `h.include?(:a) && h.include?(:b) && h.include(:c)`?

I just came up with a couple of ways.

1. The most common way - check all the elements:

  ```ruby
  [:a, :b, :c].all? {|k| h.key?(k)}
  ```

2. Use `Hash#values_at`:

  ```ruby
  h.values_at(:a, :b, :c).include?(nil) # => false
  ```
3. Subtract two arrays for comparison:

  ```ruby
  ([:a, :b, :c] - h.keys).empty? # => true
  ```
