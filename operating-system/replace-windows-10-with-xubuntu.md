# Replace Windows 10 with Xubuntu

Personal experience on installing Xubuntu 18.04 on Windows 10:

1. Create a bootable USB drive (on Ubuntu)

  1.1 Download a proper release image from the [official site](http://ftp.uni-kl.de/pub/linux/ubuntu-dvd/xubuntu/releases/18.04/release/).

  1.2 Install a `usb-creator` package to create a startup disk using the image (`usb-creator-gtk` for GNOME and `usb-creator-kde` for KDE).

  1.3 Insert a USB, choose the proper image and the device.

2. Change boot priority order on Windows 10

  2.1 Insert the bootable USB.

  2.2. Restart the computer and interrupt the booting sequence to enter BIOS setup.

  2.3  Choose `Boot -> Priority order`, move `USB CD` to the first position over the default hard drive.

  2.4 Save and exit BIOS setup.

  2.5 Restart and choose `Xubuntu`.
