# Multi-display Config with `xrandr`

`xrandr` is a tool that allows for live (re)configuration of the X server.

The following command can be used to list the configurations for all the currently detected monitors:

```console
$ xrandr --verbose
```

According to the output, the monitors can be configured with commands like:

```
$ xrandr --output HDMI-1 --mode 1920x1080 --rate 60 --primary --output VGA-1 --mode 1280x1024 --rotate left
```

Notice that not all the connected monitors can be displayed, if we encounter the error "xrandr: cannot find crtc for output <name\>", it's probably because we have more outputs than CRTCs (Cathode Ray Tube Controller). This can be checked with:

```console
$ xrandr --listproviders
```
