# Data Binding

The [Android Data Binding Library](https://github.com/googlesamples/android-databinding) is used to bind the views in the layout with data objects.

Usage:

1. Enable data binding in `build.gradle`:

  ```gradle
  android {
  // ...
      dataBinding {
          enabled = true
      }
  // ...
  }
  ```

2. In the layout file `activity_sample.xml`, add `<layout></layout>` tag around the layout.

3. Define the binding variable inside a `data` element as follows:

  ```xml
  <layout>
    <data>
      <variable
          name="sample"
          type="com.myapp.data.Sample" />
    </data>

    <!-- UI layout's root element -->
  </layout>
  ```

4. Run `gradle build`, a binding class called `ActivitySampleBinding` will be generated in `path/to/app/build/generated/source/apt/debug/edu/kit/fridget/databinding`.

5. In the activity class, we can use `DataBindingUtil` to define the binding:

  ```java
  ActivitySampleBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_sample);
  ```