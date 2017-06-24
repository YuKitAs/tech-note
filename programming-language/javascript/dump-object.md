# Dump Object

When logging a javascript object with `console.log(obj)` returns `[object Object]`, one could try to use

```javascript
console.log("%o", obj);
```
for browsers that support object dumping.
