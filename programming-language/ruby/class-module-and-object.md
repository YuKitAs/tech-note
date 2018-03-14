# Class, Module and Object

In Ruby, there are some interesting facts about the relationship between `Class`, `Module` and `Object`.

1. The top-level class is `BasicObject`, so everything is a kind of `BasicObject`.

  ```ruby
  Class.superclass #=> Module
  Module.superclass #=> Object
  Object.superclass #=> BasicObject
  ```

  From above we can see, `Class` and `Module` are both `Object`, and `Class` is a kind of `Module`.

2. `Class`, `Module` and `Object` are all instances of `Class`.

```ruby
Class.class #=> Class
Module.class #=> Class
Object.class #=> Class
```

3. The concepts and usages of `Class` and `Module` are quite similar. It's recommend to use `Module` when we want our code to be mixed (`include`) somewhere else or need specific namespace. Use `Class` when we want our code to be instantialized or inherited.


## Reference

* Paolo Perrota (2010). *Metaprogramming Ruby 2*.
