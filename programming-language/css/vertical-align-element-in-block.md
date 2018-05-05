# Vertical Align Element in Block

The CSS property `vertical-align` sounds a little misleading, it actually only specifies the vertical alignment of an inline element like:

```html
<div>Hello <span>World</span></div>
```

What I usually want is to vertically align an element in block like:

```html
<div class="header">
  <div class="title">Hello World</div>
</div>
```

with the following styling (in order to illustrate the effect):

```css
.header {
	height: 50px;
	background-color: black;
}

.title {
	color: white;
}
```

There are several tricks to vertically center the title in the header.

## Calculating padding/margin manually

If we know the heights of both parent and child elements and they are fixed, we can

1. calculate the paddings around the title:

  ```css
  .title {
    padding-top: 15px;
    padding-bottom: 15px;
  }
  ```
2. use relative position with calculated margin:

  ```css
  .header {
  	position: relative;
  }

  .title {
  	position: absolute;
    top: 50%;
    margin-top: -10px;
  }
  ```

## Using flexbox

For child elements with unknown/unfixed heights, it's more convenient to use flexbox:

```css
.header {
	display: flex;
  flex-direction: column;
  justify-content: center;
}
```
