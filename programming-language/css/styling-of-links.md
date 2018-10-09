# Styling of Links

There are four states of links:

* `a:link`: normal, unvisited
* `a:visited`: visited
* `a:hover`: mouse hover
* `a:active`: pressed

So we can change the default color accordingly like:

```scss
a:visited {
  color: $primary-color;
}
```

Remove the default underline decoration:

```css
a {
  text-decoration: none;
}
```
