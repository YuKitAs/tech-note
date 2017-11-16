# Test with `flush`

`flush` ensures that asynchronous changes have taken place, so always wrap the test in `flush` if the element template contains `dom-repeat` or `dom-if`, or if the test involves shadow DOM mutation. A `done` argument should be used in the test function to indicate it's asynchronous, and `done()` should be called at the end of `flush`. For example:

```javascript
var element, items;

setup(function() {
    element = fixture('basic');
  });
  
test('Item lengths should be equal', function(done) {
    flush(function() {
      items = element.shadowRoot.querySelector('#el');
      assert.equal(element.items.length, items.length);
      
	  done();
    });
  });
)};
```