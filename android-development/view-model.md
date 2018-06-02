# View Model

In Android, the `ViewModel` abstract class is designed to store and manage UI-related data in a lifecycle conscious way.

Dependencies:

```gradle
implementation 'android.arch.lifecycle:viewmodel:1.1.1' // for ViewModel
implementation 'android.arch.lifecycle:extensions:1.1.1' // for ViewModelProviders
```

Bind view model in the activity:

```java
ActivitySampleBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_sample);
SampleViewModel viewModel = ViewModelProviders.of(this).get(SampleViewModel.class);
binding.setViewModel(viewModel);
```
