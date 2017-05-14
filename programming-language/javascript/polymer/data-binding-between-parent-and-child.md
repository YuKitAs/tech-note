# Data Binding Between Parent And Child

Suppose we have defined a child element with two-way data binding:

```html
<dom-module id="child">
    <template>
        <custom-el value="{{prop}}"></custom-el>
    <template>

    <script>
        Polymer({
            is: 'child',

            properties: {
                prop: {
                    type: Number,
                    notify: true
                }
            }
        });
    </script>
</dom-module>
```
Now we want to include the child element in a parent element, here is a way how to bind the property of the child with the property of the parent:

```html
<dom-module id="parent">
    <template>
        <child prop="{{prop}}"></child>
        <div>[[prop]]</div>
    <template>

    <script>
        Polymer({
            is: 'parent',

            properties: {
                prop: {
                    type: Number
                }
            }
        });
    </script>
</dom-module>
```

And we can access the `prop` property in `javascript` functions:

```javascript
function getProp() {
    return document.querySelector('parent').prop;
}
```
