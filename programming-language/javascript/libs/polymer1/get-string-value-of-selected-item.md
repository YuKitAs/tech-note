# Get String Value of Selected Item

When playing with [paper-dropdown-menu](https://www.webcomponents.org/element/PolymerElements/paper-dropdown-menu/paper-dropdown-menu), I found it not easy to get the string values of the selected items. After several experiments on data binding, I finally figured out an approach without any binding.

First of all, the components are defined as follows:

```html
<paper-dropdown-menu label="...">
    <paper-listbox class="dropdown-content" id="list-box" selected="0">
        <paper-item>Choice1</paper-item>
        <paper-item>Choice2</paper-item>
        <paper-item>Choice3</paper-item>
    </paper-listbox>
</paper-dropdown-menu>
```

We need to add an event listener on the `paper-listbox` like:

```html
<script>
    document.addEventListener("WebComponentsReady", function () {
        document.querySelector("#list-box").addEventListener("iron-select", function () {
            // The action of getting the string value
        });
    });
</script>
```
The `iron-select` event will be fired whenever an item is selected.

According to the API of [paper-listbox](https://www.webcomponents.org/element/polymerelements/paper-listbox/paper-listbox), the `selectedItem` property is an `Object`. Since the string values are stored between `<paper-item>` tags, we can get them with `Node.innerText`:

```javascript
var selectedStringValue = document.querySelector("#list-box").selectedItem.innerText;
```
