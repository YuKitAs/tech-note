# Call C Function From Nasm

An `add` function in `main.c`:

```c
int add(int a, int b) {
    return a + b;
}
```

Call `add` and `printf` functions in `add.asm`:

```asm
extern add
extern printf

global _start

section .data
        format db "%d", 10, 0

_start:
        push 2
        push 3
        call add
        push eax
        push format
        call printf
        push 0

        mov eax, 1
        int 0x80
```

Compile and link as follows (on 64-bit system):

```console
$ gcc -Wall -c -m32 main.c
$ nasm -f elf add.asm
$ ld -m elf_i386 main.o add.o -lc -I /lib/ld-linux.so.2 -o add
$ ./add
5
```
