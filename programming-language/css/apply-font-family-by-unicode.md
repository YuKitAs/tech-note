# Apply Font Family by Unicode

The basic idea is to use `@font-face` with `unicode-range`. For example, we want to only apply a specific font-family to the `&` character in the following `<div>` element:

```html
<div>Hello & World!</div>
```

We can define a `@font-face` in stylesheet as follows and apply it to the `<div>` element to see the effect:

```css
@font-face {
  font-family: 'Sansation';
  src: url(sansation_light.woff);
  unicode-range: U+26;   /* unicode for & */
}

div {
  font-family: Sansation, sans-serif;
}
```

By this way it's easy to apply desired font families to special characters.
