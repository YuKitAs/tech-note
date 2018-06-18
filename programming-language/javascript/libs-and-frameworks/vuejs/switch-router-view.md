# Switch Router View

In a Vue.js project, there will be an `index.js` in the `router` folder with imported `vue-router` by default:

```javascript
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
  // path definition
})
```

The `Router` is already imported in `main.js` by default.

Now suppose our first view is defined as `FirstView.vue` and we want to switch to the next view called `NextView.vue` on button click, firstly we need to import these two components and define the paths:

```javascript
export default new Router({
  routes: [
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/',
      name: 'FirstView',
      component: FirstView
    },
    {
      path: '/next',
      name: 'NextView',
      component: NextView
    }
})
```

Then, in `App.vue`, add `<router-view/>` to the proper position in the template.

In the `FirstView` component, we could use `router-link` to do the job, but now as we want to use a button, we can define it by adding a `tag` like:

```javascript
<router-link to="/next" tag="button">Next</router-link>
```

Here comes another question, what if we don't want to switch the view directly, but do some extra work first on button click? Then we can just leave the normal `button` and set the `$router` programmatically:

```javascript
<button @click="switchNextView()">Next</button>

switchNextView() {
  // do some fancy work
  this.$router.replace('/next')
}
```
