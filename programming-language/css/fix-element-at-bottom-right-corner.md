# Fix Element at Bottom Right Corner

To place an element at the bottom right corner of the container regardless of the position of other elements. The structure looks something like this:

```html
<div class="container">
  <div>some text</div>
  <div class="bottom-right">item</div>
</div>
```

One of the best practices for styling:

```css
.container {
  position: relative;
}

.bottom-right {
  position: absolute;
  bottom: 0;
  right: 0;
}
```

However, this could probably cause the element to be overlapped on another element or displayed on the same line with others, if we want the element to be strictly below others, consider using Flexbox like:

```css
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.bottom-right {
  align-self: flex-end;
  text-align: right;
}
```
