# Type Introspection

Type introspection is a feature like `instanceof` in Java, which checks if an object belongs to a particular class or a subclass of that class, or a class implements a particular interface. In Ruby, the Object class (`Class`) provides two different methods `Object#instance_of?` and `Object#kind_of?` for checking the instance's class.

`instance_of?` checks if an instance belongs to a particular class only. `kind_of?` (synonymous of `is_a?`) checks in addition if an instance belongs to a *subclass of that class*.

Simple examples (biologically not 100% correct, just to show the difference):

```ruby
Wolf = Class.new
Dog = Class.new Wolf # Dog < Wolf
arctic_wolf = Wolf.new
husky = Dog.new

arctic_wolf.instance_of? Wolf #=> true
husky.instance_of? Dog #=> true
husky.instance_of? Wolf #=> false

arctic_wolf.kind_of? Wolf #=> true
husky.kind_of? Dog #=> true
husky.kind_of? Wolf #=> true
```
