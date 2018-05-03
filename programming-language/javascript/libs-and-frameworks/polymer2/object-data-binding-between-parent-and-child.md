# Object Data Binding Between Parent And Child

The following example shows how to bind the `Object` property with all the subproperties between a parent element and its child. 

Now I've defined a property `pokemon` with two subproperties `name` and `color`:

```javascript
static get properties() {
   return {
       pokemon: {
           type: Object,
           value: {"name": "Pikachu", "color": "Yellow"}
       }
   }
}
```

In the child element, a property `kumpel` which we want to bind with `pokemon` is defined as follows:

```javascript
static get properties() {
    return {
        kumpel: {
            type: Object,
            notify: true
        }
    };
}
```

Here I used a `paper-button` in the child element to log the value of `kumpel`:

```html
<template>
    <paper-button raised on-tap="_showKumpel">Kumpel anzeigen</paper-button>
</template>

<script>
    _showKumpel() {
        console.log(this.kumpel.color + " " +  this.kumpel.name);
    }
</script>
```

In the parent element, bind `pokemon` to `kumpel` of the child element like:

```html
<child-el kumpel="{{pokemon}}"></child-el>
```

When we click the `Kumpel anzeigen` button, we can get `"Yellow Pikachu"` as console output.

More important is, if we want to change the value of a subproperty of `pokemon`, we must use the `set` method to make an observable change to a subproperty like:

```javascript
this.set('pokemon.color', 'blue');
```

## Reference

* [Set a property or subproperty by path](https://www.polymer-project.org/2.0/docs/devguide/model-data#set-path)
