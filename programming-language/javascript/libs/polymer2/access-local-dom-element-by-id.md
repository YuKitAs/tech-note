# Access Local DOM Element by Id

According to documentation of Polymer 1.0, `$$` method provides a shorthand for `Polymer.dom(this.root).querySelector()`. `this.$$(selector)` returns the first node encountered in the local DOM that matches `selector`.

However, in Polymer 2.0, it's recommended to use `this.shadowRoot.querySelector()` instead. And it's safer to rely on the element's id than name. For example, we can use `this.shadowRoot.querySelector('#foo')` to access the `my-el` element in the local DOM of `x-el`:

```javascript
<dom-module id='x-el'>
  <template>
    <my-el id="foo"></my-el>
  </template>
</dom-module>
```