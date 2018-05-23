Vaadin ComboBox with Item Template

[Vaadin ComboBox](https://www.webcomponents.org/element/vaadin/vaadin-combo-box/elements/vaadin-combo-box) is an element of the [Vaadin Components](https://vaadin.com/components) combining with an input field and a dropdown list.

The following example shows how to use `<vaadin-combo-box>` with a custom item template:

```html
<vaadin-combo-box id="combobox" item-label-path="value" item-value-path="index" items="[[items]]" on-value-changed="_onSelect">
    <template>
        <div>[[item.index]] - [[item.name]]</div>
        <div>[[item.value]]</div>
    </template>
</vaadin-combo-box>

Selected: <span id="selected"></span>

<script>
_onSelect() {
  // Using Polymer
  this.$.selected.innerHTML = this.$.combobox.value;
}
</script>
```

The `items` is an array of objects like:

```
[{index: 0, name: "foo", value: "Hello world"},
{index: 1, name: "bar", value: "Goodbye world"}]
```

According to the template, the dropdown menu items will be displayed as:

```
0 - foo
Hello world

1 - bar
Goodbye world
```

The attribute `item-label-path` is used to define the displayed label when we selected an item. In this example it would be `item.value`, that is `Hello world` or `Goodbye world`.

The attribute `item-value-path` specifies the selected String value for the selected item, here is `item.index`. So we'll only see `Selected: 0` or `Selected: 1`.
