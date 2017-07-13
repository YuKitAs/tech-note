# Render JSON to HTML

Assume we have a JSON object `data` and we want to display the formatted content on a web page. Firstly we need to convert it to a (formatted) JSON String by using [`JSON.stringify()`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify):

```javascript
JSON.stringify(data, null, 4);
```

The third parameter indicates the number of space characters to use as white spaces.

Then we can render the returned JSON String to HTML inside `<pre>` tags because `<pre>` defined preformatted text, the javascript code would be like:

```javascript
this.$.pre.innerHTML = JSON.stringify(data, null, 4);
```
