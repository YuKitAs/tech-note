# Add Foreign Key for Model

In Rails 5, generating a child model with attribute `parent_model:references` will automatically set up the foreign key in the child table. We can find the following definition in the child migration:

```ruby
t.references :parent_model, foreign_key: true
```

Thus in the child model class, we only need to add `belongs_to :parent_model` to indicate the association, no need to add an additional `foreign_key` option.

After `db:migrate`, the child table will contain a column called `parent_model_id`.
