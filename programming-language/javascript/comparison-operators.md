# Comparison Operators

A common question in JavaScript is the difference between `==` and `===`.

Actually, `==` is an **equality operator** and `===` is an **identity operator**. That means, when using `===`, the types of two variables must be the same, but if they are not, `==` will do necessary type conversions. For example, the following conditions will all be true when using `==`:

```javascript
'0' == 0
'' == 0
'0' == false
null == undefined
new String('Hello world') == 'Hello world'
```

So it's recommended always to use `===` for comparisons instead of `==` in JavaScript.
