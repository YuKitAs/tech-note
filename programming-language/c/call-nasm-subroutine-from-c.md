# Call Nasm Subroutine From C

Here is an example showing how to call the Nasm subroutine `add` with arguments in `main.c`:

```c
#include <stdio.h>

extern int add(int, int);

int main(void) {
    printf("Result: %d\n", add(2, 3));
    return 0;
}
```
The `add.asm` is coded as follows:

```asm
global add

add:
    push ebp
    mov  ebp, esp
    push ebx
    mov  eax, [ebp+8]
    mov  ebx, [ebp+12]
    add  eax, ebx
    pop  ebx
    pop  ebp
    ret
```

Then we can compile and link the files and run it to check the result:

```console
$ nasm -f elf -o add.o add.asm
$ gcc -m32 -o main main.c add.o
$ ./main
Result: 5
```

Since we are attempting to link a 32-bit object file on a 64-bit system, adding `-m32` can create a 32-bit executable. In case there comes an error `/usr/include/features.h|374|fatal error: sys/cdefs.h: No such file or directory`, try to install the package `libc6-dev-i386`.
