# Simple Data Binding

## Binding annotations

* One-way delimiters which support downward data flow only (from host to target): `[[binding]]`
* Two-way or "automatic" delimiters which support both upward and downward data flow: `{{binding}}`

## Data binding in local DOM template

```html
<dom-module id="host-element">
    <template>
        <target-element target-property="{{value}}"></target-element>
        <target-element target-attribute$="[[value]]"></target-element>
    </template>
</dom-module>
```

Property binding results in:

```javascript
element.property = value;
```

While attribute binding is always one-way (see [Document](https://www.polymer-project.org/1.0/docs/devguide/data-binding#attribute-binding)) and results in:

```javascript
element.setAttribute(attribute, value);
```

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
    ...
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

### paper-listbox

If we want to bind the items of the listbox to an array,
we should use the `template repeater`, which creates an instance of the template's content for each item in the array. Here is an example:

```html
<template>
    <paper-listbox class="dropdown-content">
        <template is="dom-repeat" items="{{pokemons}}" as="pokemon">
            <paper-item>{{pokemon.name}}: {{pokemon.type}}</paper-item>
        </template>
    </paper-listbox>
</template>
...
<script>
    Polymer({
        is: "...",

        properties: {
            pokemons: {
                type: Array,
                value: function() {
                    return [
                        {name: "Bulbasaur", type: "Grass"},
                        {name: "Charmander", type: "Fire"},
                        {name: "Squirtle", type: "Water"},
                        ...
                    ];
                }
            }
        }
    });
</script>
```
