# Install And Use Polymer Elements

The recommended way to install Polymer elements is through [Bower](https://bower.io/). When we install a new component, Bower makes sure its dependencies are installed as well.

After installing `Bower` and `Polymer CLI`:

1. Install Polymer elements with Bower in the root of the project:

    ```console
    $ bower install --save <package_name>
    ```

    `bower install` will add a `bower_components/` folder in the root of the project. Use `--save` to add the item as dependencies in `bower.json`. An example package name is `PolymerElements/paper-elements`.

2. Load the web components polyfill library `webcomponents-lite.min.js` which provides `polyfill support`:

    ```html
    <script src="bower_components/webcomponentsjs/webcomponents-lite.min.js">
    </script>
    ```

3. Use HTML Import to link the elements, for example:

    ```html
    <link rel="import" href="../bower_components/paper-elements/paper-elements.html">
    ```

4. Declare the elements and configure the attributes, for example:

    ```html
    <paper-input label="input with at most 200 characters" char-counter maxlength="200"></paper-input>
    ```
