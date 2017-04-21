# Simple Data Binding

## Biding annotations

* One-way delimiters which support downward data flow only (from host to target): `[[binding]]`
* Two-way or "automatic" delimiters which support both upward and downward data flow: `{{binding}}`


### paper-input

Define the target property `value` of `<paper-input>`:
```html
<paper-input label="..." value="{{inputValue::change}}"></paper-input>
```

`value="{{text::change}}"` links the `inputValue` property with `<paper-input>.value` and listens for `change` event, so that Polymer will update `inputValue` whenever the input value changes.

Define the host property `inputValue`:

```html
<script>
  Polymer({
    is: "...",
    properties: {
      inputValue: {
        type: String,
        notify: true,
        value: null
      }
    }
  });
</script>
```

To bind to text content, simply include the annotation inside the target element, like:

```html
<template>
  <div>[[inputValue]]</div>
</template>
```

### paper-dropdown-menu

Similar to paper-input, bind the host property `selectedValue` to the target property `selected-item-label`:

```html
<paper-dropdown-menu label="..." selected-item-label="{{selectedValue}}">
</paper-dropdown-menu>
```

Define the host property `selectedValue`:

```html
<script>
  Polymer({
    is: "...",
    properties: {
      selectedValue: {
        type: String,
        notify: true,
        value: null
      }
    }
  });
</script>
```
