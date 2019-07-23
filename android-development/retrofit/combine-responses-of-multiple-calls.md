# Combine Responses of Multiple Calls

```kotlin
fun getObjectA(): Single<ObjectA>
fun getObjectB(): Single<ObjectB>

disposable.add(Observable.zip<ObjectA, ObjectB, Unit>(
         apiService.getObjectA(),
         apiService.getObjectB(),
         BiFunction { objA, objB ->
             // do something with objA and objB
         })
         .subscribeOn(Schedulers.io())
         .observeOn(AndroidSchedulers.mainThread())
         .subscribe({
             // do something after objA and objB are both processed
         }, {
            Log.e(TAG, "Some errors occurred")
        }))
```
