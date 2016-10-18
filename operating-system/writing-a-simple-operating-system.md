# Writing a Simple Operating System #

First of all, we will write a 512-byte boot sector named `boot.S`. Here is an example written in GNU assembly:

```gas

.code16
.text
  .global _start
  
_start:               # conventionally recogized as entry point
  mov %cs,%ax
  mov %ax,%ds
  mov %ax,%es
  
                      # string-printing routine
                      
  mov $bootMsg,%ax
  mov %ax,%bp
  mov $len,%cx
  mov $0x1301,%ax
  mov $0x000c,%bx
  mov $0,%dl
  int $0x10                 # call kernel to print chars

hang:
  jmp hang                  # infinite loop
  
bootMsg: 
  .ascii  "Hello, world!\n"
  len = . - bootMsg         # length of the message string
  
.org 510                    # pad remainder of boot sector with zeros
.byte 0x55                  # the standard PC boot signature
.byte 0xaa                  # the standard PC boot signature

```

Then we are going to build our OS. Use the following commands to compile `boot.S`:

```

as -o boot.o boot.S 
ld -Ttext=0x7c00 --oformat binary -o boot boot.o

```

`-Ttext=0x7c00` is used to set up 4K stack space after this bootloader.

Install QEMU and we can boot our simple OS from hard disk:

```
qemu-system-i386 -hda boot -boot c -m 256

```