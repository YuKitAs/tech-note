# JSON String Object Conversion

JSON String:

```java
String json = "{\"name\":\"John Doe\",\"age\": 42,\"emails\" : [\"john.doe@gmail.com\", \"doe.john@web.de\"]}";
```

## Convert JSON string to arbitrary JSON object using external library

* [`org.json.json`](https://mvnrepository.com/artifact/org.json/json):

```java
JSONObject jsonObject = new JSONObject(json);
String name = jsonObject.getString("name");
int age = jsonObject.getInt("age");
JSONArray emails = jsonObject.getJSONArray("emails");
```

* [`net.minidev.json-smart`](https://mvnrepository.com/artifact/net.minidev/json-smart):

```java
JSONObject jsonObject = (JSONObject) JSONValue.parse(json);
String name = jsonObject.getAsString("name");
int age = getAsNumber("age").intValue();
JSONArray emails = (JSONArray) jsonObject.get("emails");
```

## Convert JSON string to Java object using `ObjectMapper`

First of all, the Java class has to have a constructor annotated with `@JsonCreator`:

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
