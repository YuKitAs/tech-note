# Draw a Circle with Smooth Border

If I directly draw a circle selection, use `Select > Border` to draw a border selection and then use `Bucket Fill Tool` to fill the border with a color, the circle won't be smooth. So use the following steps instead:

1. Use `Ellipse Select Tool` and draw a circle selection.

2. Choose `Select > To Path` to convert the selection to path.

3. Choose `Select > None` to unselect the circle, because it's already converted to path.

4. Open `Edit > Stroke Path`. Here we can choose `Stroke line` with `Solid color`, `Antialiasing`, appropriate line width and foreground color. If we have set the `Paintbrush` with appropriate hardness and size, we can also choose `Paintbrush` in `Stroke with a paint tool` to achieve similar effect.
