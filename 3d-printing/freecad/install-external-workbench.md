# Install External Workbench

1. From v0.17.9940, use `Tools > Addon manager`

2. Manual install: download the workbench manually (see all available FreeCAD Addons in [GitHub repo](https://github.com/FreeCAD/FreeCAD-addons)), unzip and save it into FreeCAD's Mod directory. In the python console, we can find FreeCAD's directory, for example:

```
>>> FreeCAD.ConfigGet("UserAppData")
'/home/yukitas/.FreeCAD/'
```

Then the unzipped workbench (e.g. `FreeCAD_FastenersWB`) should be saved to `~/.FreeCAD/Mod`.
