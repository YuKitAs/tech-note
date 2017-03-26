# Linked List Data Structure

## Linear singly linked List

* Node structure:

```c
typedef struct node {
    int data;
    struct node * next;
} node_t;
```

* Linked list structure:

```c
typedef struct {
    node_t * head;
    size_t size;
} linked_list_t;
```

## Linear doubly linked List

* Node structure:

```c
typedef struct node {
    int data;
    struct node * next;
    struct node * prev;
} node_t;
```

* Linked list structure is same as `Linear singly linked list`.

## Circular singly linked list

* Node structure is same as `Linear singly linked list`.

* Linked list structure:

```c
typedef struct {
    node_t * head;
    node_t * tail;
    size_t size;
} linked_list_t;
```

## Circular doubly linked list

* Node structure is same as `Linear doubly linked list` and linked list structure is same as `Circular singly linked list`.
