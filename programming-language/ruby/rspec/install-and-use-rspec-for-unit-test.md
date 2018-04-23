# Install and Use RSpec for Unit Test

Prerequisites: `rake`, `rspec` and `rubocop` (installation tutorial in `README.md`)

1. Create a `.rspec` file in the project root with the following content:

  ```
  --require spec_helper
  ```

2. Initialize `rspec` by running

  ```console
  $ rspec --init
  ```

  Now a new directory called `spec` will be created with a `spec_helper.rb` file inside.

3. Create a test file called `<class_name>_spec.rb` in the `spec` directory.

4. At the beginning of the test file, require the file containing the class to be tested:

  ```ruby
  require "path/to/class_name"
  ```
  
  If the file path cannot be found, try to create a file called `initialize.rb` with the following content:
  
  ```ruby
  $LOAD_PATH.unshift(__dir__) unless $LOAD_PATH.include?(__dir__)
  ```
  
  and require this file in `spec_helper.rb`.
  
5. Write the test part:

  ```ruby
  RSpec.describe ClassName do
    =begin
    test methods
    =end
  end
  ```

6. Run tests:

  ```console
  $ rspec spec
  ```

## RSpec in Rails Project

Install the gem `rspec-rails` and then run:

```console
$ rails g rspec:install
```
  
Two helper files `spec_helper.rb` and `rails_helper.rb` will be created in the `spec` directory. The `rails_helper` should require `spec_helper`. The `spec_helper` is used to set up RSpec and `rails_helper` sets up the Rails stack. We can substitute `spec_helper` with `rails_helper` in `.rspec`.
