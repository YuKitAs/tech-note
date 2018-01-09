# Shadow DOM and Shady DOM

## DOM
The DOM (Document Object Model) is a programming interface for HTML and XML documents. It represents the document as nodes and objects so that programs can change the document structure. For example, we can use `document.getElementByTagName('div')` to return a list of all the `<div>` elements in the document.

## Shadow DOM
Shadow DOM can be considered as a scoped subtree inside an element. In Polymer, Shadow DOM lets us place the children in a scoped subtree (a shadow tree), so document-level CSS can't restyle the button by accident. For example:

```html
<my-element>
  #shadow-root
  <header>
    <h1>
	<button>
```

The root of the shadow tree is a _shadow root_. `<my-element>` is called the _shadow host_, which has a `shadowRoot` property referring to the shadow root. The shadow root has a `host` property that identifies its host element.

The shadow tree is separate from the element's `children`. We can add a shadow tree by using `Element.attachShadow()` like:

```html
var shadowRoot = document.createElement('div').attachShadow({mode: 'open'});
shadowRoot.innerHTML = '<h1>Hello World!</h1>';
```

Polymer provides a declarative mechanism for adding a shadow tree using `DOM template`. Polymer attaches a shadow root for each instance of the element and copies the template contents into the shadow tree:

```html
<dom-module id="my-element">
  <template>
    <style>
	/* CSS placed here is scoped to the shadow tree */
	</style>
	
    <header>
      <h1>...</h1>
      <button>...</button>
    </header>
  </template>
</dom-module>
```

Only for `host` element, the style rule inside the shadow tree matches an element outside it.

## Shady DOM

As shadow DOM is not available on all platforms, Polymer uses shady DOM and shady CSS polyfills to emulate shadow DOM. ShadyDOM provides a shim for [Shadow DOM v1](https://developers.google.com/web/fundamentals/web-components/shadowdom?hl=en).

More reference: 
1. [Polymer 2.0 documentation](https://www.polymer-project.org/2.0/docs/devguide/shadow-dom).
2. [Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Shadow_DOM), MDN web docs.