# Retrofit and RxJava

## Combine responses of two HTTP calls

Returns an Observable that emits the results of a specified combiner function applied to combinations of two items emitted, in sequence, by two other ObservableSources.

```kotlin
Observable.zip<ObjectA, ObjectB, Unit>(
         apiService.getObjectA(),
         apiService.getObjectB(),
         BiFunction { objA, objB ->
             // do something with objA and objB
         })
         .subscribeOn(Schedulers.io())
         .observeOn(AndroidSchedulers.mainThread())
         .subscribe({
             // do something
         }, {
            Log.e(TAG, "Some errors occurred")
         })
```

For three to nine calls use `Function3` to `Function9`.

## Combine responses for every item in a collection

Waits until all SingleSource sources provided by the Iterable sequence signal a success value and calls a zipper function with an array of these values to return a result to be emitted to downstream.

```kotlin
Single.zip(ids.stream().map { id ->
    apiService.getObjectById(id)
}.collect(Collectors.toList()).asIterable()) { obj -> obj }
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe({
            // do something
        }, {
            Log.e(TAG, "Some errors occurred")
        })
```
