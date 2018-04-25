# Symbol to Proc

In Ruby people use something like `array.map(&:method_name)` to call a method on every element in the array. For example, the following codes are functionally equivalent:

```ruby
['a', 'b', 'c'].map { |letter| letter.upcase } # => ["A", "B", "C"]
['a', 'b', 'c'].map(&:upcase.to_proc) # => ["A", "B", "C"]
['a', 'b', 'c'].map(&:upcase) # => ["A", "B", "C"]
```

The `&` operator will turn the symbol object (here the method name) into a block. Ruby provided `Symbol#to_proc`, it works like this:

```ruby
class Symbol
  def to_proc
    Proc.new { |x| x.send(self) }
  end
end
```

but also accepts more than one parameter:

```ruby
[1, 2, 3].inject(0, &:+) # => 6
```
