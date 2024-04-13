# Component Phases

React components have three phase: mounting, updating and unmounting for creation, change and removal.

When a component is mounted, 4 methods are called in the following order:

1. `constructor()`: may call the super constructor with the props object
2. `getDerivedStateFromProps()`: used only when the state depends on the changes to props
3. `render()`
4. `componentDidMount()`: invoked immediately after a component is mounted or inserted into the DOM tree

When a component is updated, 5 methods are called in the following order:

1. `getDerivedStateFromProps()`
2. `shouldComponentUpdate`: default returns true
3. `render()`
4. `getSnapshotBeforeUpdate()`: invoked just before the changes are rendered, any value returned will be passed as a parameter to the `componentDidUpdate()` method
5. `componentDidUpdate()`: invoked immediately after updating

When a component is unmounted, `componentWillUnmount()` will be called.
