# Basic Syntax

1. How to print `Hello world`?

  ```typescript
  console.log('Hello world');
  ```

2. How to define variables, how to print `Hello + variable`?

  ```typescript
  let name = 'Jun';
  console.log(`Hello ${name}`);
  ```

3. Which data types does it have?

  ```
  string, number, any
  ```


4. How to use `if`?

  ```typescript
  if (name && name.trim()) {
    console.log(`Hello ${name}`);
  } else {
    console.log('Hello world');
  }
  ```

5. How to loop?

  ```typescript
  let arr = [1, 2, 3];
  for (let i in arr) {
    console.log(i); // 0, 1, 2
  }

  for (let e of arr) {
    console.log(e); // 1, 2, 3
  }
  ```

6. How to define a function?

  ```typescript
  function add(x: number, y: number): number {
    return x + y;
  }

  let add = function(x: number, y: number): number {
    return x + y;
  }

  let add: (x: number, y: number) => number = function(x, y) {
    return x + y;
  }
  ```

7. How to define a class with attributes and methods?

  ```typescript

  ```

8. How to define a class constructor?

  ```typescript

  ```

9. How to extend a class and implement an interface?

  ```typescript

  ```

10. How to call the constructor of the super class?

  ```typescript

  ```

11. How to use libraries?


12. How to handle exceptions?
