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

  * Build-in primitive types:
    ```
    boolean, number, string, bigint, symbol, null, undefined, object
    ```

  * Other basic types:

    * array (`T[]` or `Array<T>`)
    * tuple (`T, T]`)
    * enum
    * unknown
    * never
    * any
    * void (subtype of `undefined`)
    * object literal (`{ property: Type }`)
    * function (`(t: T) => U`)


  In Typescript, a set is just a *set of values* that share something in common. A particular value can belong to multiple sets at the same time.

  See [advanced types](https://www.typescriptlang.org/docs/handbook/advanced-types.html).


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

7. How to define a class with constructor, attributes and methods?

  ```typescript
  class Pokemon {
    private name: string;

    constructor(name: string) {
      this.name = name;
    }

    greet() {
      console.log(`Hello, I'm ${this.name}.`);
    }
  }
  ```

8. How to extend a class, call the constructor of the super class, override a method of the super class?

  ```typescript
  class Pikachu extends Pokemon {
    constructor(name: string) {
      super(name);
    }

    greet() {
      super.greet();
      console.log("Pika pika!");
    }
  }

  let pikapi = new Pikachu("Pikapi");
  pikapi.greet();
  ```

9. How to implement an interface?

  Typescript's type system is structural but not nominal.

  ```typescript
  interface Coordinate {
    x: number;
    y: number;
  }

  interface Address {
    name: string;
  }

  function getCoord(coord: Coordinate) {
    console.log(coord.x + ", " + coord.y);
  }

  function getAddr(addr: Address) {
    console.log(addr.name);
  }

  const myLocation = {
    x: 2,
    y: 3,
    name: 'Somewhere on the earth'
  };

  getCoord(myLocation); // myLocation implemented Coordinate
  getAddr(myLocation); // myLocation implemented Address
  ```

10. How to use libraries?

  Import a module:

  ```typescript
  const fastify = require("fastify");
  const { fastify } = require("fastify");
  import fastify = require("fastify");
  import * as Fastify from "fastify";
  import { fastify, FastifyInstance } from "fastify";
  import fastify from "fastify";
  import fastify, { FastifyInstance } from "fastify";
  ```

11. How to handle exceptions?

  ```typescript
  try {
    throw new Error('Something went wrong');
  } catch(e) {
    console.log(e);
  }
  ```
