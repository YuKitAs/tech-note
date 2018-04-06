# Scope Gate and Shared Scope

In Ruby, scopes can be defined by three keywords `module`, `class` and `def`, it means each module, class and method has its own scope, and they can only access the variables inside the scope. The example below shows a variable defined outside the scope gate `def` cannot be seen from the inside:

```ruby
x = 42
def my_method
  puts x
end

my_method # => undefined local variable or method `x' for main:Object
```

So, if we want to share variables with different scopes, we need to flatten the scopes instead of using the scope gate keywords:

```ruby
x = 42
# instead of `class MyClass`
MyClass = Class.new do
  puts "Class definition: #{x}"

  # instead of `def my_method`
  define_method :my_method do
    puts "Method definition: #{x}"
  end
end

MyClass.new.my_method
```
