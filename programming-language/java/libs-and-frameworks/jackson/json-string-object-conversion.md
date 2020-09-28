# JSON String Object Conversion

JSON String:

```java
String json = "{\"name\":\"John Doe\",\"age\": 42,\"emails\" : [\"john.doe@gmail.com\", \"doe.john@web.de\"]}";
```

## Convert JSON string to arbitrary JSON object using [`org.json`](https://mvnrepository.com/artifact/org.json/json)

```java
JSONObject jsonObject = new JSONObject(json);
String name = jsonObject.getString("name");
int age = jsonObject.getInt("age");
JSONArray emails = jsonObject.getJSONArray("emails");
```

## Convert JSON string to Java object using `ObjectMapper`

```java
public class User {
    private final String name;
    private final int age;
    private final Set<String> emails;

    @JsonCreator
    public User(@JsonProperty("name") String name, @JsonProperty("age") int age,
            @JsonProperty("emails") Set<String> emails) {
        this.name = name;
        this.age = age;
        this.emails = emails;
    }

    // getters
}
```

```java
User user = new ObjectMapper().readValue(json, User.class);
String name = user.getName();
int age = user.getAge();
Set<String> emails = user.getEmails();
```

## Convert Java object to JSON string using `ObjectMapper`

```java
new ObjectMapper().writeValueAsString(user);
```
