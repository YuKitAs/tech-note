# `class_eval` and `instance_eval`

`class_eval` and `instance_eval` evaluate a string containing arbitrary code or a given block in the context of a particular class or instance. To demonstrate their usages let's take a look at the following examples. We have a `Pokemon` class defined as follows:

```ruby
class Pokemon
  def initialize(name)
    @name = name
  end

  private
  def secret_move
    "Himitsu"
  end
end
```

## `class_eval`

`ClassName.class_eval` is used to dynamically define an instance method. We can use `class_eval` to add a method to the `Pokemon` class which works on all its instances:

```ruby
Pokemon.class_eval do
  def say_hello
    "#{@name}: Konnichiwa!"
  end
end

pikachu = Pokemon.new("Pikachu")
pikachu.say_hello #=> "Pikachu: Konnichiwa!"

pachirisu = Pokemon.new("Pachirisu")
pachirisu.say_hello #=> "Pachirisu: Konnichiwa!"
```

## `instance_eval`

`ClassName.instance_eval` is used to dynamically define a class method:

```ruby
Pokemon.instance_eval do
  def say_goodbye
    "Sayounara!"
  end
end

Pokemon.say_goodbye #=> "Sayounara!"
```

`instance_name.instance_eval` allows you to access instance variables and private methods:

```ruby
pikachu.instance_eval { @name } #=> "Pikachu"
pikachu.instance_eval { secret_move } #=> "Himitsu"
```

We can also use `instance_name.instance_eval` to add a method which works only on a particular instance:

```ruby
pikachu.instance_eval do
  def move
    "Thunderbolt!"
  end
end

pikachu.move #=> "Thunderbolt!"
```

## `instance_exec`

`instance_exec` is similar to `instance_eval`, but it allows you to pass argument to the block:

```ruby
pikachu.instance_exec(80) { |pt| move.concat(" Damage: #{pt}") } #=> "Thunderbolt! Damage: 80"
```

When we want to access variables defined outside the scope of the `self` object, we can use `instance_exec` instead of `instance_eval` to get these variables.
