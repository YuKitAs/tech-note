# Vertical Alignment

## Vertical align inline elements

The `vertical-align` property can be used to align inline elements like `<span>`, `<img>` in blocks or table-cells. For example, to vertically center the text `Hello World!` in the middle of a `<div>` block:

```html
<style>
span {
  vertical-align: middle;
}
</style>
...
<div><span>Hello World!</span></div>
```

Another way is to use the `line-height`. If the height of the block is fixed (like a button or a header), we could set the `line-height` of the block to the same value of its height, like:

```html
<style>
div {
  height: 50px;
  line-height: 50px;
}
</style>
```

## Vertical align non-inline elements with `flexbox`

For non-inline child elements with unknown/unfixed heights, it's pretty convenient to use `flexbox` like:

```html
<style>
.parent {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
...
<div class="parent">
  <div class="child">Hello World!</div>
  <div class="child">Goodbye World!</div>
</div>
```

## Vertical align elements in the page with `transform`

To vertically center an element in the page is a little bit tricky. So far the best way I found is to use `transform` like:

```html
<style>
.parent {
  height: 100vh;
  position: relative;
}

.child {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
}
</style>
```
