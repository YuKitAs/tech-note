# Ruby Development Environment Setup

## Atom packages
* linter
* linter-rubocop
* rubocop-auto-correct

## Gems
1. Install Bundler using Gem 
```console
$ gem install bundler
```

2. Create `Gemfile` with the following content in the project root:

```
source 'https://rubygems.org'
gem "rake"
gem "rspec"
gem "rubocop"
```

3. Install required gems using Bundler:

```console
$ bundle install
```
