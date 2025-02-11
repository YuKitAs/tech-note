# Check Power Supply ThinkPad

On ThinkPad, battery status can be checked with `upower`:

```console
$ upower -i /org/freedesktop/UPower/devices/battery_BAT0
```

If `upower` is not installed, the voltage and power consumption (`energy-rate`) can also be checked directly with

```console
$ cat /sys/class/power_supply/BAT0/voltage_now # voltage in µV
$ cat /sys/class/power_supply/BAT0/power_now # power in µW
```

Or in more readable format:

```console
$ awk '{print $1 / 1000000 " V"}' /sys/class/power_supply/BAT0/voltage_now
$ awk '{print $1 / 1000000 " W"}' /sys/class/power_supply/BAT0/power_now
```
