# Basic Usage of `app-route`

Here I'm showing an example of `app-route 2.0.2` for polymer 2.0. According to the [official document](https://www.webcomponents.org/element/PolymerElements/app-route), this web component is still in beta at the moment.

It's common that `app-route` is used together with `app-location`. `app-location` will produce and update a `route` object when the current URL changes, and pass `route` to `app-route`:

```javascript
<app-location route="{{route}}"></app-location>

<app-route
    route="{{route}}"
    pattern="/:page"
    data="{{routeData}}"></app-route>
```

When the `route.path` String property matches the `pattern` defined in `app-route`, `app-route` will set or update its `data` Object property corresponding to the parameters in `pattern`. For example, if `route.path` is `'/test-page'`, the value of `data` would be `{"page": "test-page"}`.

I've created two elements and used `iron-pages` for selecting a page to show:

```javascript
<iron-pages selected="[[page]]" attr-for-selected="name">
    <page1-view name="page1"></page1-view>
    <page2-view name="page2"></page2-view>
</iron-pages>
```

`attr-for-selected="name"` means the `page` value would be matched to the `name` attributes of the children pages.

`page` property is defined as the official polymer demo indicates:

```javascript
page: {
    type: String,
    reflectToAttribute: true,
    observer: '_pageChanged'
}
```
It has an observer `_pageChanged`, which will be implemented later to import `page1-view.html` and `page2-view.html`.

I've also added two `paper-buttons` with anchor tags:

```javascript
<a href="page1"><paper-button raised>Page One</paper-button></a>
<a href="page2"><paper-button raised>Page Two</paper-button></a>
```

When one of the buttons is clicked, the URL will change, the `route` object will be generated or updated and passed to `app-route` (`route.page` would be like `'/page1'` or `'/page2'`), then the `routeData` will be updated as mentioned above (`routeData.page` would be like `"page1"` or `"page2"`), so we need to define an observer for `routeData` to get the current `routeData.page` value:

```javascript
static get observers() {
    return [
        '_routePageChanged(routeData.page)'
    ];
}
```

In this way we can define multiple observers in an array. It could also be normally defined in the `routeData` property.

In the following function, if `routeData.page` is not null or empty or undefined, `page1` or `page2` will be set to the `page` value, otherwise set `page1` manually:

```javascript
_routePageChanged(page) {
    this.page = page || 'page1';
}
```

Once the `page` value is updated, its observer function will be called:

```javascript
_pageChanged(page) {
    var resolvedPageUrl = this.resolveUrl(page + '-view.html');
    Polymer.importHref(resolvedPageUrl, null, null, true);
}
```

In the meanwhile, the binded `page` value in `iron-pages` will also be updated, thus one of the children will be selected and shown, as the corresponding HTML file will be imported.
