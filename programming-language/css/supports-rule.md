# `@supports` Rule

The `@supports` is used to specify CSS feature fallback depending on browser's support, which is called _feature query_. It can be combined with keywords `or`, `and`, `not`. For example:

```css
.el {
  display: grid;
  ...
}

@supports not (display: grid) {
  .el {
    display: flex;
    ...
  }
}
```

The purpose here is, apply `display: flex` alternatively whenever browser doesn't support `display: grid`.

However, if the browser doesn't support `@supports` either, neither `display: grid` nor `display: flex` would work. So a better practice would be:

```css
.el {
  display: flex;
  ...
}

@supports (display: grid) {
  .el {
    display: grid;
    ...
  }
}
```
