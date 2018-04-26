# Getting Started

The first impression: it looks similar to Polymer - take a look at the simple example below.

```html
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>

<body>
<div id="app">
    <h3>{{title}}</h3>

    <input id="input">
    <button v-on:click="onClick">Send!</button>
    <div>{{message}}</div>
</div>

<script>
    var app = new Vue({
        el: '#app',
        data: {
            title: 'Hello Vue!',
            message: ''
        },
        methods: {
            onClick: function () {
                this.message = "Message: " + input.value
            }
        }
    })
</script>
</body>
</html>
```
