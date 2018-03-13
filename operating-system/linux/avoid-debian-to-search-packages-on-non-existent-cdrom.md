# Avoid Debian to Search Packages on Non-existent CDROM

When using `apt-get` to install default packages, I got the following message:

```
Media change: please insert the disc labeled
 'Debian GNU/Linux 9.3.0 _Stretch_ - Official amd64 DVD Binary-1 <timestamp>'
in the drive '/media/cdrom/' and press [Enter]
```

Because there is such a paramter in `/etc/apt/sources.list` by default, indicating a local CDROM as a package source, but it's actually not available. So I need to modify the file by commenting this parameter out like:

```
# deb cdrom:[Debian GNU/Linux 9.3.0 _Stretch_ - Official amd64 DVD Binary-1 <timestamp>]/ stretch contrib main
```
