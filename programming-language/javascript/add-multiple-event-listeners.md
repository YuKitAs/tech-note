# Add Multiple Event Listeners

In pure JS, it's not possible to pass multiple events as the first parameter for `addEventListener()`, a trick is to use an array of events like:

```javascript
["click", "touchstart"].forEach(ev =>
  element.addEventListener(ev, () => {
    // do something
  }, false)
);
```
