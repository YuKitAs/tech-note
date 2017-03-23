# Function Pointer

Say we want a function to change an integer number through a user-defined method, it's defined with two parameters: an integer pointer `int *p` which points to the integer number, and a function pointer `void (*funcPtr) (int *)` which points to the user-defined method:

```c
void changeNum(int *p, void (*funcPtr) (int *)) {
    (*funcPtr) (p);
}
```

Then we define an `increaseNum` function as follows:

```c
void increaseNum(int *p) {
    (*p)++;
}
```

Now we can call `changeNum` with `increaseNum`:

```c
int i = 42;
int *p;
p = &i;

changeNum(p, increaseNum);
```
