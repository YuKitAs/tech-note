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

4. Run

```console
$ rspec --init
```

Now a `spec` directory with a `spec_helper.rb` file will be created.

5. Create test files in the `spec` directory.

6. At the beginning of the test file, require the file containing the class we want to test with `require_relative 'path/to/filename'`, and the tests can be written like:

```ruby
RSpec.describe AnyClass do
=begin
  test methods
=end
end
```
