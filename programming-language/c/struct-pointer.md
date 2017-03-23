# Struct Pointer

We have a struct defined as follows:

```c
typedef struct {
    int a;
    int b;
} simpleStr;
```

Now we are going to create an instance of the struct in a function, initialize the members and return a struct pointer:

```c
simpleStr *generateStruct(int a, int b) {
    simpleStr *p = malloc(sizeof(simpleStr));
    p->a = a;
    p->b = b;

    return p;
}
```

It is important to use `malloc` so that the struct variable will be allocated in the heap segment, because local variables in the stack segment will be unavailable once the function finishes execution.
