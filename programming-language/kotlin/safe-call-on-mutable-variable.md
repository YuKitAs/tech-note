# Safe Call on Mutable Variable

Unlike Java, the following code:

```kotlin
var someVar: VarType? = null

fun doSomething() {
  if (someVar != null) {
    someCollection.add(someVar)
  }
}
```

will arouse compilation error:

```
Smart cast to 'VarType' is impossible, because 'someVar' is a mutable property that could have been changed by this time
```

which means, the value of `someVar` could be assigned to null on a different thread between the execution of the null check and the add operation.

## Workaround 1: use immutable local variable

```kotlin
val immutableVar = someVar
if (immutableVar != null) {
  someCollection.add(immutableVar)
}
```

## Workaround 2: use a safe call

with `let` keyword:

```kotlin
someVar?.let{ someCollection.add(it) }
someVar?.let(someCollection::add)
```

with Elvis operation `?:`:

```kotlin
someCollection.add(someVar ?: return)
```
