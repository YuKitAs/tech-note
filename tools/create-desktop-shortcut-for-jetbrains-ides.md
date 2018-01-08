# Create Desktop Shortcut For JetBrains IDEs

In Linux, after downloading and untaring a JetBrains IDE one can only run it from the shell script. If we want to create a desktop shortcut, the simplest way is to set `Tools > Create Desktop Entry` in IDE menu.

It will create a shortcut in the system menu, usually under `Development`, then we can choose `Add to Desktop`.

A more common way is to create a `*.desktop` file under `~/.local/share/applications` (for personal use) or `/usr/share/applications` (for all users). Take `jetbrains-rubymine.desktop` for example, edit the file as follows:

```
[Desktop Entry]
Version=1.0
Type=Application
Name=RubyMine
Icon=path/to/RubyMine-2017.3.1/bin/RMlogo.svg
Exec="path/to/RubyMine-2017.3.1/bin/rubymine.sh" %f
Comment=The Drive to Develop
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-rubymine
```
