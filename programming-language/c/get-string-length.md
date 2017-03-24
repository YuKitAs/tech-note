# Get String Length

To get the length of a string variable (without the terminating `\0` character) in C, we can simply use the `strlen()` function from `<string.h>`:

```c
char * string = "Hello world!"
int len = strlen(string);
```

And if we don't want to use `strlen()`, we can use a loop instead:

```c
char * string = "Hello world!"
int len = 0;
while(string[len] != '\0') len++;
```
