# Capture Argument Values

In some situation we want to verify a method argument, e.g. the DTO to save for a repository:

```java
userRepository.save(user);
```

`ArgumentCaptor<T>`  is used to capture argument values for further assertions.

```java
ArgumentCaptor<User> userCaptor = ArgumentCaptor.forClass(User.class);
verify(userRepository).save(userCaptor.capture()); // the capture() method must be used inside of verification

User userToSave = userCaptor.getValue(); // returns the latest captured value; for varargs use getAllValues()
assertThat(userToSave.getName()).isEqualTo("foo");
```

`ArgumentCaptor` can be auto-created with the `@Captor` annotation:

```java
@Captor
ArgumentCaptor<User> userCaptor;
```
