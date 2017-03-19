# Diassemble C to Nasm

1. Use `gcc` to generate an object file from the source code file `main.c`:

```console
gcc -fno-asynchronous-unwind-tables -s -c -o main.o main.c
```

`-fno-asynchronous-unwind-tables` means do not generate unnecessary sections like `.eh_frame`. `-s` means remove all symbol table and relocation information from the executable.

2. Use `objconv` to generate a `main.asm` file:

```console
objconv -fnasm main.o
```

`objconv` can be downloaded from [here](http://www.agner.org/optimize/). Extract `source.zip` and run `build.sh`, move the generated `objconv` executable into `/bin`.

3. Fix the `nasm` code manually. For example, remove the `default rel` line and all `align=N` and `execute`/`noexecute` text.
