# Select Element by Attribute Pattern

* `[attr^='foo']`: matches all `attr` starting with `foo`

* `[attr$='foo']`: matches all `attr` ending with `foo`

* `[attr*='foo']`: matches all `attr` containing `foo`

For example:

```javascript
document.querySelectorAll("[class*='button']").forEach(el => {
  // do something
});
```
