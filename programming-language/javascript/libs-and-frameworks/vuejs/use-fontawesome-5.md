# Use Font Awesome 5

In Font Awesome 5, only Font Awesome Brands (prefix `fab`) and Font Awesome Solid (prefix `fas`) are free to use. So we can install the  following packages with Yarn:

```console
$ yarn add @fortawesome/fontawesome-svg-core
$ yarn add @fortawesome/free-solid-svg-icons
$ yarn add @fortawesome/vue-fontawesome
```

Next, we need to import components from these packages in a Vue project configured with `vue-cli`. For example, we want to use a solid style icon from [Font Awesome](https://fontawesome.com/icons?d=gallery&s=solid) with `class="fas fa-kiwi-bird"`, we should add it in `main.js` like:

```javascript
import Vue from 'vue'
import App from './App'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faKiwiBird } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faKiwiBird)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  /* ... */
})
```

And in the `vue` file where we want to use the icon:

```vue
<template>
  <font-awesome-icon icon="kiwi-bird"/>
</template>

<script>
export default {
  /* ... */
}
</script>
```
