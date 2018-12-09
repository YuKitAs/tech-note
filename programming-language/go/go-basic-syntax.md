# Go Basic Syntax

The following are some general aspects only.

1. How to print `Hello world`?

  ```go
  package main

  import "fmt"

  func main() {
    fmt.Println("Hello world")
  }
  ```

2. How to define variables, how to print `Hello + variable`?

  Static type declaration:

  ```go
  var name string
  name = "Bonbon"
  fmt.Println("Hello " + name)
  ```

  Dynamic type declaration:

  ```go
  name := "Bonbon"
  fmt.Println("Hello " + name)
  ```

  Constant and formatting:

  ```go
  const NAME string = "Bonbon"
  fmt.Printf("Hello %s", NAME)
  ```

3. Which data types does Go have?

  ```
  * Boolean (true, false)
  * Numeric (Integer, Float)
  * String
  * Derived types (Pointer, Array, Structure, Union, Function, Slice, Interface, Map, Channel)
  ```

4. How to use `if`?

  ```go
  var name string
  if name != "" {
    fmt.Println("Hello " + name)
  } else {
    fmt.Println("Hello void")
  }
  ```

  If with a short statement before the condition, variables defined in this statement are also available in the `else` block:

  ```go
  var name string
  if greet := "Hello "; name != "" {
    fmt.Println(greet + name)
  } else {
    fmt.Println(greet + "void")
  }
  ```

5. How to loop?

  Basic `for` loop:

  ```go
  sum := 0
  for i := 0; i < 10; i++ {
    sum += i
  }
  fmt.Println(sum)
  ```

  `for` that is equivalent to `while`:

  ```go
  sum := 0
  i := 1
  for i < 10 {
    sum += i
    i++
  }
  fmt.Println(sum)
  ```

6. How to define a function?

  ```go
  func greet(name string) string {
    greet := "Hello "
    if name != "" {
      return greet + name
    }
    return greet + "void"
  }

  func main() {
    fmt.Println(greet("Bonbon"))
  }
  ```


7. How to define a class with attributes and methods?

  Go provides structs instead of classes:

  ```go
  type Pet struct {
    name string
    species string
    age int
  }

  func main() {
    pet := Pet {
      name: "Bonbon",
      species: "Djungarian hamster",
      age: 1,
    }

    fmt.Printf("%s is a %d-year-old %s.\n", pet.name, pet.age, pet.species)
  }
  ```

  Output:

  ```
  Bonbon is a 1-year-old Djungarian hamster.
  ```

8. How to define a class constructor?

  Go uses `New()` function instead of constructors. Define a package:

  ```go
  package pet

  import "fmt"

  type pet struct {
    name string
    species string
    age int
  }

  func New(name string, species string, age int) pet {
    return pet {name, species, age}
  }

  func (pet pet) Info() {
    fmt.Printf("%s is a %d-year-old %s.\n", pet.name, pet.age, pet.species)
  }
  ```

  The method names are capitalized because they will be exported.

  Then in the `main` package, import the `pet` package and create a `pet` instance:

  ```go
  func main() {
    pet := pet.New("Bonbon", "Djungarian hamster", 1)
    pet.Info()
  }
  ```

9. How to extend a class and how to implement an interface?

  A type can't be simply extended in another package. Type embedding is something similar to inheritance in the Go world.

  The parent package with exported struct and fields:

  ```go
  type Pet struct {
    Name string
    Species string
    Age int
  }
  ```

  Import the parent package in the child package and define the struct:

  ```go
  type MyPet struct {
    pet.Pet
  }
  ```

  Then the child can be instantialized and is able to access the fields and methods of the parent:

  ```go
  myPet := MyPet {
    Pet: pet.Pet {
      Name: "Bonbon",
      Species: "Djungarian hamster",
      Age: 1,
    },
  }

  fmt.Printf("%s is a %d-year-old %s.\n", myPet.Name, myPet.Age, myPet.Species)
  ```

  An interface is implemented implicitly like:

  ```go
  type Pet interface {
  	Info()
  }

  type MyPet struct {
  	Description string
  }

  // This means MyPet implements the interface Pet without using any keyword
  func (myPet MyPet) Info() {
  	fmt.Println(myPet.Description)
  }
  ```

10. How to call the constructor of the super class?

  See 8 and 9.

12. How to handle exceptions?

  Use the `errors` package:

  ```go
  import "errors"

  func validate(num int) error {
    if num < 0 {
      return errors.New(fmt.Sprintf("Negative number: %v", num))
    }

    return nil
  }

  func main() {
    result := validate(-1)
    if result != nil {
      fmt.Printf("[ERROR] %s\n", result)
    }
  }
  ```

  Output:

  ```
  [ERROR] Negative number: -1
  ```

13. How to do unit tests?

  To test a simple function:

  ```go
  package sum

  func Sum(x, y int) int {
    return x + y
  }
  ```

  Name a test package `sum_test.go`, import the `testing` package and the `sum` package:

  ```go
  func TestSum(t *testing.T) {
    result := sum.Sum(2, 3)
    if result == 5 {
      t.Logf("Sum: %d", result)
    } else {
      t.Errorf("Sum incorrect.\nExpected: %d\nActual: %d", 5, result)
    }
  }
  ```

  Notice there is no assertion, non-failing information can be logged on debug level.

  Run the following command to execute all the tests in the current directroy (logs will only be output in verbose mode):

  ```console
  $ go test -v
  ```

  Output:

  ```
  === RUN   TestSum
  --- PASS: TestSum (0.00s)
      sum_test.go:11: Sum: 5
  PASS
  ok
  ```
