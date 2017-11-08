# Basic Usage of Templating

[mustache.js](https://github.com/janl/mustache.js/) is a popular JavaScript templating engine. I'll show you a simple example on how to use it. The latest version can be accessed through `https://cdnjs.cloudflare.com/ajax/libs/mustache.js/2.3.0/mustache.js`.

Basically we need to define two variables: a `view` object and a `template` string. `view` object contains the data and code we want to render, `template` contains any number of mustache tags:

```javascript
var data = {
      "players": [
          {"name": "Pikachu", "move": "Thunderbolt", "power": function () { return Math.floor((Math.random() * 100) + 1) }},
          {"name": "Raichu", "move": "Thunder", "power": 100}
      ],
      "enemy": {
          "name":"Magikarp"
      }
    }

var template = "{{#players}} {{name}} used {{move}}. {{enemy.name}} got {{power}} points of damage.<br> {{/players}}"

var output = Mustache.render(template, data);
```

`Mustache.render()` takes these two variables as parameters and returns a string, which in this example would be:

```
Pikachu used Thunderbolt. Magikarp got 74 points of damage.
Raichu used Thunder. Magikarp got 100 points of damage.
```

If the `players` key does not exist, or has a value of `undefined`, `null`, `false`, `0`, `NaN` or is empty, the block `{{#players}}...{{/players}}` will not be rendered at all.
