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
  
  Instead, using `rake test` can also run RuboCop after running RSpec.

