# Data Binding Between Parent And Child

Suppose we have defined a child element with a two-way data binding:

```html
<dom-module id="child">
    <template>
        <custom-el value="{{myProp}}"></custom-el>
    <template>

    <script>
        Polymer({
            is: "child",

            properties: {
                myProp: {
                    type: Number,
                    notify: true
                }
            }
        });
    </script>
</dom-module>
```
Now we want to include the child element in a parent element and bind the `myProp` property of the child to the parent:

```html
<dom-module id="parent">
    <template>
        <child my-prop="{{myProp}}"></child>
        <div>[[myProp]]</div>
    <template>
</dom-module>
```

If we write unit test for the parent we can see that the parent already has the `myProp` property without defining it again. So we can access the `myProp` property directly from the parent in `javascript` functions:

```javascript
function getMyProp() {
    return document.querySelector("parent").myProp;
}
```
