# Basic Syntax

Compile and run:

```console
rustc main.rs
./main
```

1. How to print `Hello world`?

  ```rust
  fn main() {
      println!("Hello world!");
  }
  ```

Using `!` means it's calling a Rust macro instead of a normal function.

2. How to define variables, how to print `Hello + variable`?

  ```rust
  fn main() {
      let name = "Jun";
      println!("Hello {}!", name);
  }
  ```

The variable is immutable by default. A mutable variable should be defined with `let mut`.

3. Which data types does it have?

  Rust is statically typed. If the type annotation is not explicitly specified, the compiler will try to infer it based on the value and how it's used.

  **Scalar types**:

  * Integer: (i|u)(8|16|32|64|128|size)
  * Float: f32, f64
  * Boolean: `let f: bool = false;`
  * Character: `let z: char = 'Z';`

  **Compound types**:

  * Tuple: `let tup: (i32, f64) = (42, 6.2)`;
  * Array:
  ```rust
  let a = [1, 2, 3];
  let a: [i32; 3] = [1, 2, 3];
  let a = [3; 5]; // [3, 3, 3, 3, 3]
  ```

4. How to use `if`?

  ```rust
  let number = 6;

  if number % 4 == 0 {
      println!("number is divisible by 4");
  } else if number % 3 == 0 {
      println!("number is divisible by 3");
  } else if number % 2 == 0 {
      println!("number is divisible by 2");
  } else {
      println!("number is not divisible by 4, 3, or 2");
  }
  ```

  Use `if` in a `let` statement:

  ```rust
  let condition = true;
  let number = if condition { 5 } else { 6 };
  ```

5. How to loop?

  The `loop` keyword is equivalent to `while (true)`. Furthermore, `while` and `for` loops with conditions:

  ```rust
  while number < 10 {
    // ...
    number += 1;
  }

  let a = [1, 2, 3];
  for element in a.iter() { ... }
  ```

6. How to define a function?

  ```rust
  fn some_func(x: i32) -> i32 { x + 1 }

  fn some_other_func(s: String) -> (String, usize) {
    let length = s.len();
    (s, len)
  }

  let y = {
    let x = 3;
    x + 1
  }
  ```

  Expressions do not include ending semicolons in order to return a value.


7. How to define a struct?

  ```rust
  struct Rectangle {
      width: u32,
      height: u32,
  }

  fn main() {
      let rect1 = Rectangle {
          width: 30,
          height: 50,
      };

      do_something(&rect1);
  }
  ```

8. How to extend and implement a trait?

  Implement a trait:

  ```rust
  pub trait Summary {
    fn summarize(&self) -> String;
  }

  pub struct Tweet {
      pub username: String,
      pub content: String,
  }

  impl Summary for Tweet {
      fn summarize(&self) -> String {
          format!("{}: {}", self.username, self.content)
      }
  }
  ```

  Some trais have basic implementations provided and are derivable (e.g. `Eq`, `Clone`, `Copy`, `Hash`, `Default`, `Debug`):

  ```rust
  #[derive(Debug)]
  struct Rectangle {
      width: u32,
      height: u32,
  }
  ```

  Extend a trait:

  ```rust
  pub trait A {}
  pub trait B: A {}
  ```

9. How to use libraries (crates)?

  Define a module:

  ```rust
  mod front_of_house {
      pub mod hosting { // exposing path with `pub`
          pub fn add_to_waitlist() {}
      }
  }
  ```

  Include module:

  ```rust
  use crate::front_of_house::hosting;

  pub fn eat_at_restaurant() {
      hosting::add_to_waitlist();
  }
  ```


10. How to handle exceptions?

  Rust uses the enum type `Result<T, E>` for *recoverable* errors and `panic!` for *unrecoverable* errors:

  ```rust
  let f = File::open("hello.txt");

  let f = match f {
    Ok(file) => file, // assign the file handle value to `f`
    Err(error) => panic!("Problem opening the file: {:?}", error); // {:?} formats a `Debug` output
  }

  let f = File::open("hello.txt").unwrap_or_else(|error| {
      if error.kind() == ErrorKind::NotFound {
          File::create("hello.txt").unwrap_or_else(|error| {
              panic!("Problem creating the file: {:?}", error);
          })
      } else {
          panic!("Problem opening the file: {:?}", error);
      }
  });
  ```

  A shortcut for the `match` above is `unwrap`. `expect` is similar to `unwrap` with a custom `panic!` error message.

  See [details](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html).


11. How to write unit tests?
