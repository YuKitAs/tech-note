# Create and Remove Start Menu Entries

On Xubuntu, start menu entries are `*.desktop` files stored in `~/.local/share/applications` with the following basic meta data:

```
[Desktop Entry]
Name=foo
Exec=/path/to/foo
Icon=/path/to/icon.png
Terminal=false
Type=Application
```

To create a desktop shortcut launcher, just make this file executable and copy it into `~/Desktop`.

## Reference

* [Desktop Entry Specification](https://developer.gnome.org/desktop-entry-spec/), GNOME Developer
