# Get Context in Fragment

As in Activity, we can use like `MainActivity.this` to get the application context,
in Fragment, we should use `getActivity().getApplicationContext()`. But notice the `getActivity()` method would return `null` and thus cause the `NullPointerException`.
