# Create Desktop Shortcut For JetBrains IDEs

In Linux, after downloading and untaring a JetBrains IDE one can only run it from the shell script. The simplest way is to create an application launcher on the desktop is to set `Tools -> Create Desktop Entry` in IDE menu. It will create a shortcut in the system menu, then choose `Add to Desktop` by right-clicking the shortcut.

A `*.desktop` file will be created under `~/.local/share/applications` or `/usr/share/applications` (for all users). Take `jetbrains-rubymine.desktop` for example, the content would be as follows:

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

As well as `Tools -> Create Command-line Launcher` for creating a command-line launcher.
