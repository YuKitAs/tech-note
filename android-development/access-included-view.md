# Access Included View

A view as follows

```xml
<TextView
    android:id="@+id/text"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

can be referenced in another view like:

```xml
<include layout="@layout/view_text" />
```

Usually, the included TextView can be accessed by its own id `R.id.text`.

If an id is specified in the `<include>` tag like

```xml
<include android:id="@+id/super_text" layout="@layout/view_text" />
```

It will override the id of the TextView, as the included content will become:

```xml
<TextView
    android:id="@+id/super_text"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

which means, now the TextView can only be accessed by `R.id.super_text` in this case. It's useful when the same view is included at several places, so they can be distinguished by different ids specified in `<include>`. 
