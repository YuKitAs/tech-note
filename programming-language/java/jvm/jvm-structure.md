# JVM Structure

## Data Types

The JVM operates on two kinds of types: *primitive* types (including *numeric*, *boolean* and *returnAddress*) and *reference* types. An object is either a dynamically allocated class or an array, a reference to an object is considered to have type *reference*.

## Run-Time Data Access
### `pc` Registers
Each JVM thread has its own pc register which contains the address of the instruction currently being executed if it's a non-native method, otherwise the pc register is undefined.

### JVM Stacks
Each JVM thread has a private JVM stack which holds local variables and partial results and can push and pop frames.

### Heap
The heap is the run-time data area for allocating memory for class instances and arrays. Heap storage for objects is reclaimed by an automatic storage management system (a.k.a gc). The heap size may be fixed or can be dynamically expanded or contracted, depending on the computation.

### Method Area
The method area is also shared among all JVM threads, it stores per-class structure such as run-time constant pool, field, method data, the code for methods and constructors. It's logically part of the heap, its size may also be fixed or can be dynamically expanded or contracted.

### Run-Time Constant Pool
The JVM maintains a per-type constant pool, a run-time data structure that serves many of the purposes of the symbol table for a conventional programming language implementation.

### Native Method Stacks
Conventional stacks ("C stacks") are used to support native methods.

## Frames
A frame is used to stored data and partial results, perform dynamic linking, return values for methods, and dispatch exceptions. A new frame is created each time a method is invoked and will be destroyed when the method invocation is complete, either normal or abrupt.
