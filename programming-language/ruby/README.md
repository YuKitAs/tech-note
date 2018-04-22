# Ruby Development Environment Setup

## Atom packages
* linter
* linter-rubocop
* rubocop-auto-correct

## Gems

1. Install RubyGems:

  ```console
  $ sudo apt install rubygems
  ```

2. Install Bundler using Gem:

  ```console
  $ gem install bundler
  ```

3. Create `Gemfile` with the following content in the project root:

  ```
  source 'https://rubygems.org'

  gem "rake"
  gem "rspec"
  gem "rubocop"
  ```

4. Install required gems using Bundler:

  ```console
  $ bundle install
  ```
  
5. (Optional) Add the following content into `Rakefile` in order to run `rspec spec` and `rubocop` with `rake test` command:

  ```ruby
  task(default: [:test])

  task :test do
    sh "rspec spec"
    sh "rubocop"
  end
  ```
