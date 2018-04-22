# Singleton Class

A singleton class in Ruby is a hidden class of object which has only one instance. It can be accessed in the following tricky way:

```ruby
obj = Object.new

singleton_class = class << obj
  self
end

singleton_class.class # => Class
```

We can define methods in the singleton class like:

```ruby
class << obj
  def a_singleton_method
    "Hello Bonbon!"
  end
end

obj.a_singleton_method # => Hello Bonbon!
```

Since classes are objects, every class has a singleton class and class methods are just instance methods of the singleton classes. So we can directly define class methods in the singleton class of class:

```ruby
class MyClass
  class << self
    def a_class_method
      "Hello Bonbon!"
    end
  end
end

MyClass.a_class_method # => Hello Bonbon!
```

It's functionally equivalent to:

```ruby
class MyClass
  def self.a_class_method
    "Hello Bonbon!"
  end
end

MyClass.a_class_method # => Hello Bonbon!
```

It's easy to understand that the superclass of the singleton class of `MyClass` is the singleton class of the superclass of `MyClass`:

```ruby
MyClass.singleton_class # => <Class:MyClass>
MyClass.singleton_class.superclass # => #<Class:Object>

MyClass.superclass # => Object
MyClass.superclass.singleton_class # => #<Class:Object>
```
