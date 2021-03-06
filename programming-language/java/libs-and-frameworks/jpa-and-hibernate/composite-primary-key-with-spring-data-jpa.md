# Composite Primary Key with Spring Data JPA

A composite key consists of multiple primary keys that can be combined to identify an entity.

This note is basically about how to store and retrieve such data with Spring Boot and Spring Data JPA. There are two different ways to specify composite keys.

## Using `@Embeddable`
1. Create an Embeddable class which has to implement `Serializable`:

  ```java
  @Embeddable
  public class MyCompositeKey implements Serializable {
      @Column(name = "key_one")
      private String key1;

      @Column(name = "key_two")
      private String key2;

      /*
      The rest omitted for simplicity
      */
  ```

2. Create the Entity class containing `@EmbeddedId` instead of `@Id`:

  ```java
  @Entity
  @Table(name = "my_entities")
  public class MyEntity {
      @EmbeddedId
      private MyCompositeKey myCompositeKey;

      @Nullable
      private String description;

      /*
      The rest omitted for simplicity
      */
  }
  ```

3. In the Repository interface, we have to explicitly write the method like:

  ```java
  Optional<MyEntity> findByMyCompositeKeyKey1AndMyCompositeKeyKey2(
          String key1, String key2);
  ```

## Using `@IdClass`

1. Create the composite key class as above without the `@Embeddable` annotation.

2. In the Entity class, mark every primary key field with `@Id`:

  ```java
  @Entity
  @Table(name = "my_entities")
  @IdClass(MyCompositeKey.class)
  public class MyEntity {
      @Id
      @Column(name = "key_one")
      private String key1;

      @Id
      @Column(name = "key_two")
      private String key2;

      @Nullable
      private String description;

      /*
      The rest omitted for simplicity
      */
  }
  ```

According to the definitions above, the table `my_entities` in MySQL would look like this:

```
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| key_one           | varchar(255) | NO   | PRI | NULL    |       |
| key_two           | varchar(255) | NO   | PRI | NULL    |       |
| key_three         | varchar(255) | NO   | PRI | NULL    |       |
| description       | varchar(255) | YES  |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
```

In addition, when handling many-to-one relationship between this Entity and another Entity, we need to join all the columns which are used for composite primary key:

```java
@Entity
@Table(name = "my_second_entities")
public class MySecondEntity {
    @Id
    private String id;

    @ManyToOne
    @JoinColumns({
            @JoinColumn(
                    name = "my_entity_key_one",
                    referencedColumnName = "key_one",
                    nullable = false),
            @JoinColumn(
                    name = "my_entity_key_two",
                    referencedColumnName = "key_two",
                    nullable = false),
            @JoinColumn(
                    name = "my_entity_key_three",
                    referencedColumnName = "key_three",
                    nullable = false
            )
    })
    @OnDelete(action = OnDeleteAction.CASCADE)
    private MyEntity myEntity;
}
```

In this way, each `my_second_entities` record will also store three columns referring to a unique record in `my_entities`.
