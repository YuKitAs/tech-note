# React Hooks

Hooks should only be called at the top level of React function components so that they can be called in the same order each time a component renders.

Some commonly used hooks are `useState`, `useEffect`, `useContext`, `useReducer` and `useCallback`.

## State

**Usage**:

```typescript
import React, { useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  // return ...
}
```

* The `useState` hook in function components is an alternative to `this.setState` in the constructor of class components

* `useState` returns the current state and a function that updates it

* When calling `setCount`, React will re-render the `Example` component and pass the new `count` value to it

* We can declare multiple state variables for different states, or declare one state with an object/array value to group them. However, updating a state variable always replaces it instead of merging it.


## Effect

**Usage**:

```typescript
import React, { useState, useEffect } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `You clicked ${count} times`;
  });

  // return ...
}
```

* Initial render: the effect will be performed after the the first render (similar to `componentDidMount`) and after every update by default, we can declare multiple effects to split concerns.

* Subsequent renders: effects can be skipped if certain values (props and states) provided as a dependency array are not changed in order to improve performance:

  ```typescript
  useEffect(() => {
    document.title = `You clicked ${count} times`;
  }, [count]); // only re-run the effect if count changes
  ```

  If no dependency array is give, the effect will run on every render; if given an empty array, it will only be run once.

* Cleanup: an effect can be cleaned up by returning an optional `cleanup()` function from the effect.

* Unmounting: if a cleanup function is present, it'll be executed before the component is unmounted.

## Reference

* [React Hooks](https://reactjs.org/docs/hooks-rules.html)
