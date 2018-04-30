# Text Overflow with Ellipsis

The following are two different cases, single-line text and a paragraph:

```html
<div>Hello world!</div>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque auctor arcu sed tristique volutpat.
</p>
```

To limit the single-line text within a certain width ending with ellipsis (`...`) is easy as pie:

```css
div {
  width: 100px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

To do the same with a paragraph is a little different, because the text is also limited by the height. The easiest solution I found on Internet is to use `-webkit-box`. For example, we can display the first three lines:

```css
p {
  width: 200px;
  display: -webkit-box;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
```

It will be shown as:

```
Lorem ipsum dolor sit
amet, consectetur
adipiscing elit. Quisq...
```

A possible problem is that in real browsers some certain characters of the last row might be cropped when using `overflow: hidden`, because these characters will bleed outside their em squares. I tried to modify the line-height but it didn't help. Changing font-size or font-family can solve this problem.

Another problem is that it only works in browsers which use `WebKit` engine, but not in eg. Firefox.
