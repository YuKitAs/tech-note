# Use AsyncTask to Make HTTP Calls with Retrofit

>AsyncTask enables proper and easy use of the UI thread. This class allows you to perform background operations and publish results on the UI thread without having to manipulate threads and/or handlers.

When I was getting started with Retrofit, I have learned how to use `AsyncTask` to make HTTP calls. The following are just some memos.

I've created normal layouts using `RecyclerView` and `CardView` in order to display a list of posts.

With a typical Retrofit client instance, I created a simple service as follows to get all the posts from my server:

```java
public interface PostService {
    @GET("posts")
    Call<List<Post>> getAll();
}
```

After configured an adapter, I wanted to call this service in `MainActivity`.

Firstly, I need to set the adapter to `RecyclerView` to display the post list fetched from server:

```java
private void generateDataList(List<Post> postList) {
    RecyclerView recyclerView = findViewById(R.id.customRecyclerView);
    PostListAdapter adapter = new PostListAdapter(postList);
    RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(MainActivity.this);
    recyclerView.setLayoutManager(layoutManager);
    recyclerView.setAdapter(adapter);
}
```

Then, create an inner class extending [`AsyncTask`](https://developer.android.com/reference/android/os/AsyncTask):

```java
private class GetPostsTask extends AsyncTask<Call<List<Post>>, Void, List<Post>> {
    private final ProgressDialog progressDialog;

    private GetPostsTask(ProgressDialog progressDialog) {
        this.progressDialog = progressDialog;
    }

    protected void onPreExecute() {
        progressDialog.setMessage("Loading....");
        progressDialog.show();
    }

    protected List<Post> doInBackground(Call<List<Post>>... calls) {
        try {
            Call<List<Post>> call = calls[0];
            progressDialog.dismiss();
            return call.execute().body();
        } catch (IOException e) {
            generateDataList(Collections.<Post>emptyList());
            Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_SHORT).show();
            return null;
        }
    }

    protected void onPostExecute(List<Post> posts) {
        generateDataList(posts);
    }
}
```

The `ProgressDialog` component above was used to show some status information in the app. I defined it in the `MainActivity` and passed it to the inner class. I called `PostService` in the `onCreate` method like:

```java
public class MainActivity extends AppCompatActivity {
  ProgressDialog progressDialog;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);

      PostService service = RetrofitClientInstance.getRetrofitInstance().create(PostService.class);
      Call<List<Post>> call = service.getAll();
      new MainActivity.GetPostsTask(progressDialog).execute(call);
  }

  /*
  private methods
  */
}
```