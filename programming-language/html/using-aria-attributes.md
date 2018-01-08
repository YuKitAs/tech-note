# Using ARIA attributes

WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Application) is a recommended webstandard published by W3C.

Web developers should use the ARIA `role` and `aria-*` attributes on HTML elements that match the [implicit ARIA semantics](https://www.w3.org/TR/html-aria/#dfn-implicit-aria-semantics).

ARIA `role` attribute is used to describe the type of widget presented, or the structure of the web page. For example

```html
<header role="banner">
<nav role="navigation">
```

The `aria-label` attribute is used to define a string that indicates the current element, when there is no visible text labeling this element. For example

```html
<button aria-label="Close" onclick="myDialog.close()">X</button>
```


More references: 
* [ARIA in HTML](https://www.w3.org/TR/html-aria/), W3C.
* [Using ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques), MDN web docs.
