# Mock Maker

[`MockMaker`](https://javadoc.io/static/org.mockito/mockito-core/3.9.0/org/mockito/plugins/MockMaker.html) is an extension for Mockito in order to use custom implementation instead of the default `byte-buddy/asm/objenesis`.

The text configuration file should be named `org.mockito.plugins.MockMaker` in `src/test/resources/mockito-extensions` so that it will be loaded by Mockito.

With the following line

```
mock-maker-inline
```

Mockito is able to mock final classes and methods, which is not allowed by default.
