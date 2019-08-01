# Exception Handling

The generic [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) objects will be thrown when runtime errors occur, they can be used to define custom exceptions. Below is an example to throw and catch a user-defined exception based on `Error`.

```javascript
const arr = [42];

try {
  console.log('Result: ' + get(1));
} catch (e) {
  if (e.name === 'index out of bound') {
    // handle error
  } else {
    // handle generic errors
  }
}

function get(index) {
  if (index >= arr.length) {
    throw new Error('index out of bound');
  }
  return arr[index]
}
```

Besides `Error`, JavaScript has seven primary [error types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#Error_types):

* **EvalError**: Creates an instance representing an error that occurs regarding the global function eval().
* **InternalError**: Creates an instance representing an error that occurs when an internal error in the JavaScript engine is thrown.
* **RangeError**: Creates an instance representing an error that occurs when a numeric variable or parameter is outside of its valid range.
* **ReferenceError**: Creates an instance representing an error that occurs when de-referencing an invalid reference.
* **SyntaxError**: Creates an instance representing a syntax error that occurs while parsing code in eval().
* **TypeError**: Creates an instance representing an error that occurs when a variable or parameter is not of a valid type.
* **URIError**: Creates an instance representing an error that occurs when `encodeURI()` or `decodeURI()` are passed invalid parameters.

These specific errors can be checked by `instanceof` like:

```javascript
if (e instanceof EvalError) {
  // handle error
}
```

A [custom error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#Custom_Error_Types) (e.g. `MyError`) with custom parameters and methods can be defined by extending the `Error` class.
