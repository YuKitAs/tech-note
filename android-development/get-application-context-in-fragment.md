# Get Application Context in Fragment

As in Activity, we can use like `MainActivity.this` to get the activity context,
in Fragment, we can use `getActivity().getApplicationContext()`to get the application context. But notice the `getActivity()` method would return `null` and thus cause the `NullPointerException`.
