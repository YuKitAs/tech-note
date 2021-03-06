# Create Shared Folder in VirtualBox

Two simple steps need to be done in order to share files between host and guest.

1. In `Settings > Shared Folders` of the VM, set a name and choose the path for the folder to share on the host computer, for example a folder named `temp`.

2. Choose a folder on the guest, e.g. `~/share`. Then use the following command:

  ```console
  sudo mount -t vboxsf temp ~/share
  ```

3. If it shows `mount: unknown filesystem type 'vboxsf'`, we need to install `VirtualBox Guest Additions`, see [this note](https://github.com/YuKitAs/tech-note/tree/master/operating-system/virtual-machine/install-virtualbox-guest-additions.md).
