# Use Database Cleaner

The gem `database_cleaner` uses a set of strategies to clean up test data stored in database.

After installed the gem, we can modify `rails_helper.rb` as follows:

```ruby
require "database_cleaner"

RSpec.configure do |config|
  # ...

  config.before(:suite) do
    DatabaseCleaner.clean_with(:truncation)
  end

  config.before(:each) do
    DatabaseCleaner.strategy = :transaction
    DatabaseCleaner.start
  end

  config.after(:each) do
    DatabaseCleaner.clean
  end
```

For SQL libraries, `Transaction` is the fastest strategy. For Mongoid, the strategies `Transaction` and `Deletion` are not supported.

## Reference

* [Database cleaner](http://databasecleaner.github.io/)
