# Pointer Receivers

A method is a function with a special receiver argument, whose type can also be pointer.

When using a struct value receiver, the method can only operate on a copy of the struct, by using a pointer to struct as the receiver, then the fields of the struct can be modified. For example:

```go
type Position struct {
  X, Y float64
}

func (pos *Position) Move(x, y float64) {
  pos.X += x
  pos.Y += y
}

func main() {
  pos := Position {0, 0}
  pos.Move(1.5, -3)
  fmt.Printf("Current position: (%v, %v)\n", pos.X, pos.Y)
}
```

Output:

```
Current position: (1.5, -3)
```

And if we change the pointer receiver to a value receiver like:

```go
func (pos Position) Move(x, y float64) {
  pos.X += x
  pos.Y += y
}
```

Then the fields won't be modified.

Output:

```
Current position: (0, 0)
```

BTW, we could also pass the struct pointer as function parameter like:

```go
func Move(pos *Position, x, y float64) {
  pos.X += x
  pos.Y += y
}

func main() {
  pos := Position {0, 0}
  Move(&pos, 1.5, -3)
  fmt.Printf("Current position: (%v, %v)\n", pos.X, pos.Y)
}
```
