# Avoid Hiding Imports

In IntelliJ, by default, when auto-formatting, the imported classes from the same package will be summarized like `c.b.a.package.*`. In order to list all the classes, go to `Settings > Code Style > Java > Imports`, set `Class count to use import with '*'` and `Names count to use static import with '*'` to 99.

`java.awt.*` and `javax.swing.*` can be made as exceptions.
