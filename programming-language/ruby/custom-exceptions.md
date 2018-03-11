# Custom Exceptions

Custom exceptions in Ruby should extent `StandardException`. The most common way to raise an exception is to use

```ruby
raise(CustomError, "this is an error message")
```

The second string parameter is optional.

Since `raise` also receives exception objects, we can write an exception class in order to raise a custom exception with argument:

```ruby
class AmountError < StandardError
  attr_reader(:amount)

  def initialize(amount)
    @amount = amount
    super("invalid amount: #@amount")
  end
end
```

Suppose we want to verify if an amount is non-negative, we can use the custom exception like this:

```ruby
def validate(amount)
  raise(AmountError.new(amount)) if amount < 0
end

validate(-1)
```

Our custom error message will be output to the console:

```console
invalid amount: -1 (AmountError)
```
