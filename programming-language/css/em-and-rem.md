# `em` and `rem`

Unlike `px`, `em` and `rem` are both relative units that are frequently used for scalable layouts. `em` is relative to the font-size of the element, `rem` ("Root EM") is relative to the font-size of the root element.

It's recommended by the W3C to use `em` for font-size. The browser's font-size is `16px` by default, so the default size of `1em` is `16px`, but it doesn't always mean the same, for example:

```css
div.a {
  font-size: 1em;
  margin-left: 1em;
}

div.b {
  font-size: 2em;
  margin-left: 1em;
}
```

Assume the font-size defined in `<html>` is `16px`. `1em` for `margin-left` in `div.a` is `16px`, but `1em` becomes `32px` in `div.b` because the font-size of `div.b` is `2em` (`32px`).

Differently, `1rem` is always equal to the browser's font-size, so it might be useful for padding and margins.
