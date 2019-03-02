# Api Service with Kotlin

In Kotlin, it's common to create a singleton Retrofit service instance using `companion object` in the interface where we declare all the request methods. An example of the interface:

```kotlin
interface ApiService {
  @GET("users/{user}/repos")
  Call<List<Repo>> listRepos(@Path("user") String user);

    companion object {
        fun create(): ApiService {
            val retrofit = Retrofit.Builder()
                    .baseUrl("https://api.github.com/")
                    .addConverterFactory(AnyConverterFactory.create())
                    .build()

            return retrofit.create(ApiService::class.java)
        }
    }
}
```
