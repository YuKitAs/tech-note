# Ruby Basic Syntax

1. How to print `Hello world`?

```ruby
puts "Hello world"
```

2. How to define variables, how to print `Hello + variable`?

```ruby
name = "Yuka"
puts "Hello #{name}"
```

3. Which data types does Ruby have?

```
* Boolean (true, false)
* Symbol (:name.methods, "name".object_id)
* Number (Fixnum, Bignum, Float, BigDecimal, rational numbers, nil)
* String ("Hello 'world'", 'Hello "world"')
* Array ([1, 2, 3])
* Hash ({ :de => "Germany", :no => "Norway"})
```

4. How to use `if`?

```ruby
def greet(name)
  if name == "Yuka"
    puts "Hello #{name}!"
  else
    puts "Hello stranger!"
  end
end
```

5. How to loop?

```ruby
def greetAll(names)
  names.each do |name|
    puts "Hello #{name}!"
  end
end
```

6. How to define a function?

```
See 4 and 5.
```

7. How to define a class with attributes and methods?

```ruby
class Greeter
  attr_accessor :names

  def initialize(names)
    @names = names
  end

  def greetAll
    if @names.nil?
      puts "Hello No One!"
    elsif @names.respond_to?("each")
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      puts "Hello #{@names}!"
    end
  end
end

names = ["Yuka", "Pichu", "Pikachu"]
greeter = Greeter.new(names)
greeter.greetAll
```

Output:

```
Hello Yuka!
Hello Pichu!
Hello Pikachu!
```

8. How to define a class constructor?

```
See 7.
```

9. How to extends a class?

```ruby
class Nager
  attr_reader :name

  def initialize(name)
    @name = name
  end

  def eat
    "nuts"
  end
end

class Squirrel < Nager
  def eat
    super + " and fruits"
  end
end
```

10. How to call the constructor from the parent class?

```ruby
class Squirrel < Nager
  def initialize()
    super("Pachirisu")
  end

  def eat
    super + " and fruits"
  end
end

pachirisu = Squirrel.new()
puts pachirisu.name + " eats " + pachirisu.eat
```

Output:

```
Pachirisu eats nuts and fruits
```

11. How to use libraries?

```ruby
require 'path/to/lib_name'
require_relative 'relative/path/to/lib_name'
```

12. How to do unit tests?

```ruby
RSpec.describe Squirrel do
  before do
    @pachirisu = Squirrel.new("Pachirisu")
  end

  it 'inherits constructor from Nagel' do
    expect(@pachirisu.name).to eq "Pachirisu"
  end

  it 'overrides eat of Nagel' do
    expect(@pachirisu.eat).to eq "nuts and fruits"
  end
end
```
