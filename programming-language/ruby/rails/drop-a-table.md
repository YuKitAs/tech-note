# Drop a Table

To drop a migrated table, we need to generate a new migration:

```console
rails g migration drop_foo
```

In the migration:

```ruby
class DropFoo < ActiveRecord::Migration
  def up
    drop_table :foo
  end

  def down
    fail ActiveRecord::IrreversibleMigration
  end
end
```

Then run `rake db:migrate` to drop the table `foo`.
