# Component Phases

React components have three main phases: mounting, updating and unmounting in which the component is created (JSX is rendered), changed and removed.

## Mounting

When a component is mounted, the component is added to the DOM, 4 methods are called in the following order:

1. `constructor()`: called before mounting, for initializing the component with props and default state, may call the super constructor with the props object.

2. `static getDerivedStateFromProps()`: used only when the state depends on the changes to props before the component is mounted.

3. `render()`: returns the JSX that represents the component's UI.

4. `componentDidMount()`: invoked immediately after a component is mounted and rendered.

* `componentWillMount()`: deprecated since React 16.3.0.

## Updating

When a component is updated, 5 methods are called in the following order:

1. `static getDerivedStateFromProps()`: updates the state based on changes in props.

2. `shouldComponentUpdate`: by default returns true, can be overridden with custom logic, if returns false, the subsequent lifecycle methods won't be executed.

3. `render()`

4. `getSnapshotBeforeUpdate()`: invoked just before the changes are rendered to capture previous props and states, any values returned will be passed as parameters to the `componentDidUpdate()` method.

5. `componentDidUpdate()`: invoked immediately after updating, commonly used for performing side effects.

## Unmounting

When a component is unmounted, it's removed from the DOM, `componentWillUnmount()` will be called.
