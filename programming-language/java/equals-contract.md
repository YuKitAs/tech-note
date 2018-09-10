# `equals` Contract

When overriding the `equals` method, it must implement an equivalence relation which has the following properties:

1. **Reflexive**: for non-null `x`: `x.equals(x)` returns `true`

2. **Symmetric**: for non-null `x` and `y`: `x.equals(y)` returns `true` if and only if `y.equals(x)` returns `true`

3. **Transitive**: for non-null `x`, `y`, `z`: if `x.equals(y)` and `y.equals(z)` return `true`, then `x.equals(z)` returns `true`

4. **Consistent**: for non-null `x` and `y`; multiple invocations of `x.equals(y)` must consistently return `true` or `false`

5. **Non-nullity**: for non-null `x`: `x.equals(null)` returns `false`
