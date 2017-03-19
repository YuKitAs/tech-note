# Write a Simple Boot Sector With Nasm

The main boot sector file `boot_sect.asm`:

```asm
[BITS 16]
[ORG 0x7c00]

MOV si, HELLO_MSG       ; store string pointer to si
CALL PRINT_STRING
INT 0x10                ; call interrupt
JMP $                   ; jump to the address of the current instruction

%INCLUDE "print_string.asm"

HELLO_MSG:
    db "Hello, world!", 0

TIMES 510-($-$$) db 0   ; $ represents the address of the current line
                        ; $$ address of the first instruction
DW 0xaa55               ; add boot signature at the end
```

`print_string.asm` with function `PRINT_STRING`:

```asm
PRINT_STRING:
    NEXT:   MOV al, [si]
            INC si
            OR al, al               ; check if the end of the string is 0
            JZ EXIT                 ; jump when "zero" flag is 1
            CALL PRINT_CHARACTER    ; otherwise print the current character
            JMP NEXT
    EXIT:   ret

%INCLUDE "print_character.asm"
```

`print_character.asm` with function `PRINT_CHARACTER`:

```asm
PRINT_CHARACTER:
    MOV ah, 0x0e
    INT 0x10
    RET
```

We can assemble our source code into machine code as follows:

```console
$ nasm boot_sect.asm -f bin -o boot_sect.bin
```

And then get it run with QEMU:

```console
$ qemu-system-i386 boot_sect.bin
```
