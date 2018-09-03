# Function as Return Type

A reusable function can be returned like (with lambda expression):

```java
static final Function<Integer, Integer> doubleFunction = input -> input * 2;
```

It's equivalent to:

```java
static final Function<Integer, Integer> doubleFunction = new Function<Integer, Integer>() {
    @Override
    public Integer apply(Integer input) {
      return input * 2;
    }
  };
```

A practical reason why returning a function instead of calling it directly is that we want to bind certain arguments to the function without declaring them as member variables and should never care about them ever after. 

For example, we have the following method, which is used to return the value found in one of the maps or `-1`:

```java
static Integer findValue(String key, Map<String, Integer> map1, Map<String, Integer> map2) {
    if (map1.containsKey(key)) {
        return map1.get(key);
    }

    if (map2.containsKey(key)) {
        return map2.get(key);
    }

    return -1;
}
```

Obviously, every time we call this method, we need to provide two maps even though they are always the same. To avoid this, we can define a method which returns a new function as follows:

```java
static final Function<String, Integer> findValueFunction(Map<String, Integer> map1, Map<String, Integer> map2) {
    return key -> findValue(key, map1, map2);
}
```

Once initialized `findValueFunction` with two maps, we can use it by simply providing only one argument:


```java
Function<String, Integer> findValueFunction = findValueFunction(map1, map2);
findValueFunction.apply("keyword");
```
