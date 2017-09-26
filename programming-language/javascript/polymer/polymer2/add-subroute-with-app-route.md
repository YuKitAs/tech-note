# Add Subroute With `app-route`

This note is an extension of [Basic Usage of app-route](https://github.com/YuKitAs/tech-note/blob/master/programming-language/javascript/polymer/polymer2/basic-usage-of-app-route.md). It's the cleanest way that I've tried so far to add subroute path to the route path, say, `'/page1/subpage1'`.

After creating a new element named `subpage1-view`, I added a `paper-button` in `page1-view` to get access to the subpage:

```javascript
<a href="/page1/page1-subpage1">
    <paper-button raised>Subpage One</paper-button>
</a>
```
Then we should add a new `app-route` in the main page for subroute, and add the `tail` attribute to the former `app-route` for route as follows:

```javascript
<app-route
        route="{{route}}"
        pattern="/:page"
        data="{{routeData}}"
        tail="{{subroute}}"></app-route>
<app-route
        route="{{subroute}}"
        pattern="/:subpage"
        data="{{subrouteData}}"
        active="{{subrouteActive}}">
</app-route>
```

The usage of the `active` attribute in `app-route` for subroute is a little tricky. Because when `subroute` changes, `subrouteData` won't be cleared (it's said to be a bug), but the `active` attribute will be `false` when `subroute.path` no longer matches the `pattern`.  So if we want to change the `page` value according to `routeData.page`, not to `subrouteData.subpage`, we could check if `subrouteActive` is `false`.

Next, add `<subpage1-view name="subpage1"></subpage1-view>` into `iron-pages` so that it can be selected to show.

Plus, we have to modify our observer by passing an extra parameter `subrouteData.subpage` to it:

```javascript
static get observers() {
    return [
        '_routePageChanged(routeData.page, subrouteData.subpage)'
    ];
}
```

In `_routePageChanged(page, subpage)`, we should decide how to set the `page` value with the help of the `subrouteActive` flag:

```javascript
_routePageChanged(page, subpage) {
    if (subpage && this.subrouteActive) {
        this.page = subpage || 'page1';
    } else {
        this.page = page || 'page1';
    }
}
```
