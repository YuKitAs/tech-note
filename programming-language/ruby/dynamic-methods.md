# Dynamic Methods

In Ruby, we can use the `send` method to send a message to an object, in order to call a specific method. The following is a simple example:

```ruby
class MyClass
  def my_method(*args)
    "Hello " + args.join(" ")
  end
end

obj = MyClass.new
obj.send(:my_method, "cruel", "world") # => "Hello cruel world"
```

As is shown above, we have sent the method name together with its arguments to an object (and its ancestors) until the `my_method` method reacts. It's called dynamic dispatching and is useful when we want to call methods dynamically.

We can use this way to define methods dynamically as well. For example, we want to get similar information about different components of an object, we don't need to repeat the `get_<component_name>_info` method for each component, instead we can use method dispatching in a static `define_component` method by the component name like this:

```ruby
class MyClass
  def initialize(id, data_source)
    @id = id
    @data_source = data_source
    # get matched component name and pass them to MyClass.define_component
    data_source.methods.grep(/^get_(.*)_info$/) { MyClass.define_component $1 }
  end

  def self.define_component(name)
    define_method(name) do
      info = @data_source.send("get_#{name}_info", @id)
      return info
    end
  end
end
```
