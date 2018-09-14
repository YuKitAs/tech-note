# Replace Windows 10 with Xubuntu

Personal experience on installing Xubuntu 18.04 on Windows 10:

1. Create a bootable USB drive (on Ubuntu)

* Download a proper release image from the [official site](http://ftp.uni-kl.de/pub/linux/ubuntu-dvd/xubuntu/releases/18.04/release/).

* Install a `usb-creator` package to create a startup disk using the image (`usb-creator-gtk` for GNOME and `usb-creator-kde` for KDE).

* Insert a USB, choose the proper image and the device.

2. Change boot priority order on Windows 10

* Insert the bootable USB.

* Restart the computer and interrupt the booting sequence to enter BIOS setup.

*  Choose `Boot -> Priority Order`, move `USB CD` to the first position over the default hard drive.

* Save and exit BIOS setup.

* Restart and choose `Xubuntu`.
