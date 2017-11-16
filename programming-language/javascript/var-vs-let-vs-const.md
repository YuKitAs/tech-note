# `var` vs. `let` vs. `const`

The key difference between `var` and `let` is that while `var` is scoped to the nearest function block, `let` is scoped to the nearest enclosing block. For example, in a function block, `var i = 0` defined in a `for()` loop is visible to the whole function, but `let i = 0` will only be visible in this loop. `let` can therefore be used to avoid closure problems.

In addition, global variables defined with `let` won't be added as properties on the global `windows` object.


[not finished]