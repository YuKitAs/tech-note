# JPA Cascade Types

`javax.persistence.CascadeType` contains the following types:

```
ALL
PERSIST
MERGE
REMOVE
REFRESH
DETACH
```

`Cascade.ALL` propagates all operations from a parent entity to a child entity.

`Cascade.REMOVE` is equivalent to `CascadeType.DELETE` from Hibernate and can only be specified for `@OneToOne` and `@OneToMany` relationships.
