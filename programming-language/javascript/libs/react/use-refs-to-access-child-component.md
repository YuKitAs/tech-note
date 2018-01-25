# Use `refs` to Access Child Component

In React, parent components can only interact with their children through `props` of the children. The child to be modified could either be an instance of a React component or a DOM element. React provides a `refs` attribute which can be attached to any child component.

Here is an example showing how `refs` works:

```javascript
class ParentComponent extends React.Component {
  doSomething() {
    // do something to `this.input`
  }

  render() {
    return (
      <div>
        <ChildComponent
          ref={input => { this.input = input; }}
          onClick={this.doSomething.bind(this)}
        />
      </div>
    );
  }
}
```

An advantage of `refs` over `id` is that the components with the same ID can't be reused. But `refs` should not be used for anything that can be done declaratively.


More reference:
* [Refs and the DOM](https://reactjs.org/docs/refs-and-the-dom.html), React Docs.
