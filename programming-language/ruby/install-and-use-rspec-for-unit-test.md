# Install and Use RSpec for Unit Test

1. Install `rubygems` and `bundler` with `apt-get`.

2. Create a `Gemfile` under project with the following content:

```
source 'https://rubygems.org'

group :test do
  gem 'rake'
  gem 'rspec'
  gem 'rubocop'
end
```

3. Run

```console
$ bundle install
```

Now `rake`, `rspec` and `rubocop` will be installed.

4. Create a `.rspec` file with the following content:

```
--require spec_helper
```

5. Run

```console
$ rspec --init
```

Now a `spec` directory with a `spec_helper.rb` file will be created.

6. Create a test file named `*_spec.rb` in the `spec` directory, 

7. At the beginning of the test file, require the file containing the class we want to test with `require_relative 'path/to/filename'`, and the tests can be written like:

```ruby
RSpec.describe AnyClass do
=begin
  test methods
=end
end
```

8. Run tests:

```console
$ rspec spec
```
