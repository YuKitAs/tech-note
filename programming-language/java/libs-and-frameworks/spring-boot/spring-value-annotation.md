# Spring Value Annotation

The `@Value` annotation is used to inject values to fields in Beans. The values can be read from default property sources (incl. properties/YAML files, environment variables and system properties) or external configurations by using `@@PropertySource`.

## Simple Values

By default, if `application.properties` contains a property in the following format:

```properties
user.name=foo
```

It can be simply read in the `@Configuration` class like:

```java
@Value("${user.name}")
private String name;

@Bean
public String getName() {
    return name;
}
```

## Array Values

To read an array value, it's only possible to use the following formats.

In `application.properties`:

```properties
user.roles=A,B,C
```

*instead of*

```properties
user.roles[0]=A
user.roles[1]=B
user.roles[2]=C
```

with

```java
@Value("${user.roles}")
private List<String> roles;
```

Or in `application.yml`:

```yaml
user:
  roles: A,B,C
```

*instead of*

```yaml
user:
  roles:
    - A
    - B
    - C
```

with

```java
@Value("#{'${user.roles}'.split(',')}")
private List<String> roles;
```

## Environment Variables

To read environment variables like `USER_NAME=FOO`:

```java
@Value("${USER.NAME}")
private String name;
```

## Default values

If the property name cannot be found in any property source, default values can be set as follows:

```java
@Value("${whatever.string:}")
@Value("${whatever.string:dummy}")
@Value("${whatever.int:42}")
@Value("${whatever.bool:false}")
@Value("${whatever.val:#{null}}")
```
