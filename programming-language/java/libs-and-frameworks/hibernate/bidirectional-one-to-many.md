# Bidirectional One-to-Many

In a relational database, a one-to-many relationship exists between two tables, with the child table using foreign keys to reference the primary key in the parent table.

The following examples show how to map a one-to-many relationship bidirectionally.

In the parent entity, use `@OneToMany` for the collection variable (e.g. `List` or `Set`) of child entities:

```java
@Entity
@Table(name = "parents")
public class ParentEntity {
    @Id
    @GeneratedValue
    private long id;

    @OneToMany(mappedBy = "parentEntity", cascade = CascadeType.ALL)
    private List<ChildEntity> children = new ArrayList<>();
}
```

To make the relationship bidirectional, it's recommended by JPA specification to use the `mappedBy` property, which indicates the variable in the child entity referencing to the parent, to mark the parent as the inverse side, and in the child entity, use `@ManyToOne` to mark the child as the owing side:

```java
@Entity
@Table(name = "children")
public class ChildEntity {
    @Id
    @GeneratedValue
    private long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_id", nullable = false)
    private ParentEntity parentEntity;
}
```

Hibernate 2 or JPA use `EAGER` as default fetching strategy for `@ManyToOne` association, which is considered to be bad for performance.

The `@JoinColumn` indicates the foreign key in the child table. If there are multiple keys, use `@JoinColumns`.

The `CascadeType.ALL` is important for inserting or updating the child table automatically when a parent record is inserted or removed.

A common use case is:

```java
ParentEntity parent = new ParentEntity();
ChildEntity child = new ChildEntity();
parent.addChild(child); // children.add(child); child.setParent(this);
// persist the parent
```
