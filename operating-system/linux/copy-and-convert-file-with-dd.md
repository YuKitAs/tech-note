# Copy and Convert File with `dd`

`dd` is a low-level copy operation with data got formatted before it's written to the destination. The basic syntax is

```
dd [if=FILE] [of=FILE] [ibs=N] [obs=N] [bs=N] [count=N] [skip=N] [seek=N] [conv=notrunc|noerror|sync|fsync]
```

An example of copying an image file to a device file:

```console
# dd if=some-image.iso of=/dev/sdX bs=4M status=progress conv=fsync
```

where `bs` (block size) means the number of bytes that are read, written, or converted at one time, it can also be written as `bs=4096`.

An example of creating an image from a disk:

```console
# dd if=/dev/sr0 of=some-image.iso bs=2M count=$(isosize -d 2048 /dev/sr0) status=progress
```
