# Object Data Binding Between Parent And Child

If we have an object property in a parent element, how can we bind this property with all the subproperties to its child element? Now I've defined a `pokemon` property with two subproperties `name` and `color`:

```javascript
static get properties() {
   return {
       pokemon: {
           type: Object,
           value: {"name": "pikachu", "color": "yellow"}
       }
   }
}
```

In the child element, we need to define the property, which we want to bind, as follows:

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

I used a `paper-button` in child element to log the value of `kumpel`:

```javascript
<template>
    <paper-button raised on-tap="_changeKumpel">Kumpel ändern</paper-button>
</template>

<script>
    _changeKumpel() {
        console.log(this.kumpel.color + " " +  this.kumpel.name);
    }
</script>
```

After both properties are defined, we bind `pokemon` to `kumpel` using `<child-el kumpel="{{pokemon}}"></child-el>`, and when we click the `Kumpel ändern` button, we can get the `"yellow pikachu"` console output, which means the entire `pokemon` property is bound to `kumpel`.

If we want to change the value of a subproperty of `pokemon`, we can use like `this.set('pokemon.color', 'blue')`, the `set` method will make an observable change to a subproperty. Now when we click the `Kumpel ändern` button, `"blue pikachu"` will be logged.
