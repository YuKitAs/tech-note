# Test Modules

Suppose we have a module as follows which we are going to include in some classes:

```ruby
module MyModule

  def greet(name)
    "Hello #{name}!"
  end
end
```

To test the module with RSpec we need to firstly define a dummy class, and then let the instance of the dummy class extend the module, so that the module methods will be added into the instance:

```ruby
class DummyClass
end

RSpec.describe MyModule do
  before(:each) do
    @dummy_class = DummyClass.new
    @dummy_class.extend(MyModule)
  end

  it 'greets' do
    expect(@dummy_class.greet("Bonbon")).to eq "Hello Bonbon!"
  end
end
```
