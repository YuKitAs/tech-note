# Install VirtualBox Guest Additions

In order to use `vboxsf` to mount shared folders in VirtualBox, `VBoxGuestAdditions.iso` should be installed.

Select `Devices > Insert Guest Additions CD image` (`Geräte > Gasterweiterungen einlegen`), if it shows `cannot mount the media/drive 'C:\Program Files\Oracle\VirtualBox\VBoxGuestAdditions.iso'` with status  `VERR_PDM_MEDIA_LOCKED`, it means there is already an ISO file. Just remove the ISO file in `Devices > CD/DVD Devices` (`Geräte > Optische Laufwerke`) and select `VBoxGuestAdditions.iso` again.

Then mount the ISO file using:

```console
$ sudo mount /dev/cdrom /mnt
```

Install the `VirtualBox Guest Additions`:

```console
$ sudo ./mnt/VBoxLinuxAdditions.run
```
