# Install and Init Polymer

`npm` is required so make sure an active LTS version of [Node.js](https://nodejs.org/en/) is installed.

1. Install `Bower` with npm:

    ```console
    $ npm install -g bower
    ```

2. Install `Polymer CLI` with npm:

    ```console
    $ npm install -g polymer-cli
    ```

3. Create a directory for the project and initialize it with:

    ```console
    $ polymer init
    ```

    After the initialization the project should contain the following files and directories:

    * bower.json
    * bower_components
    * demo/index.html
    * index.html
    * my-el.html
    * test/my-el_test.html


We can also create a `bower.json` file with

```console
$ bower init
```


The content of `my-el.html` should somehow look like this:

```javascript
<link rel="import"  href="path/to/bower_components/polymer/polymer.html">

<dom-module id="my-el">
    <template>
        <style></style>
    // here is the local DOM part
    </template>

    <script>
    Polymer({
      is: "my-el",

      properties: {}
    });
    </script>
</dom-module>
```

The content of the test file should look like this:

```javascript
<!doctype html>
<html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, minimum-scale=1, initial-scale=1, user-scalable=yes">

    <title></title>
    
    <script src="path/to/webcomponentsjs/webcomponents-lite.js"></script>
    <script src="path/to/web-component-tester/browser.js"></script>

    <link rel="import" href="path/to/my-el.html">
    </head>

    <body>
    <test-fixture id="basic">
        <template>
            <my-el></my-el>
        </template>
    </test-fixture>

    <script>
        suite("my-app-element", function() {
        test("instantiating the element works", function() {
            var element = fixture("basic");
            assert.equal(element.is, "my-el");
        });
        });
    </script>
    </body>
</html>
```

And we can define more tests in the `my-app-element` suite.
