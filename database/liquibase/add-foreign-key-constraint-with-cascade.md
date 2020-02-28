# Add Foreign Key Constraint with Cascade

1. On creating table:

```yaml
- createTable:
  tableName: some_table
  columns:
    - column:
      name: some_col
      type: varchar(100)
      constraints:
        primaryKey: true
        nullable: false
        foreignKeyName: fk_some_col_to_another_col
        references: another_table(another_col)
        deleteCascade: true
```

2. Adding constraint separately:

```yaml
- addForeignKeyConstraint:
    baseColumnNames: some_col
    baseTableName: some_table
    constraintName: fk_some_col_to_another_col
    onDelete: CASCADE
    referencedColumnNames: another_col
    referencedTableName: another_table
    validate: true
```
