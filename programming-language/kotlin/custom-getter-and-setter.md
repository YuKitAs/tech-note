# Custom Getter and Setter

In Kotlin, getters and setters are optional. Without any declaration there will be default getter and setter for `var` property and getter for `val` property. If more logic required, custom getter and setter can be defined as follows:

```kotlin
var counter = 0 // might with initial value
  set(value) {
    if (value > 0) field = value
  }

val isEmpty: Boolean
  get() = this.size == 0
```

In the setter example, `field` is an identifier keyword.
