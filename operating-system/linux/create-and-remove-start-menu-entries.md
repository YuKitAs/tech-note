# Create and Remove Start Menu Entries

In `~/.local/share/applications`, create a `*.desktop` file with the following basic meta data:

```
[Desktop Entry]
Name=foo
Exec=/path/to/foo
Icon=/path/to/icon.png
Terminal=false
Type=Application
```

To create a desktop shortcut launcher, we can copy this file into `~/Desktop`. However, if the desktop shortcut is deleted, we need to remove the entry from start menu by deleting the corresponding `*.desktop` file in `~/.local/share/applications`.

## Reference

* [Desktop Entry Specification](https://developer.gnome.org/desktop-entry-spec/), GNOME Developer
