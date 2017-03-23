# Struct Pointer

We have a struct defined as follow:

```c
typedef struct {
    int a;
    int b;
} simpleStr;
```

Now we are going to create an instance of the struct in a function, and return a struct pointer:

```c


simpleStr *generateStruct(int a, int b) {
    simpleStr *p = malloc(sizeof(simpleStr));
    p->a = a;
    p->b = b;

    return p;
}
```

It is important to use `malloc` so that the `struct` variable will be stored in the heap segment, because local variables allocated in the stack segment will be unavailable once the function finishes execution.
