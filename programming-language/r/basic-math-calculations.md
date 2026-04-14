# Basic Math Calculations

* **Factorial (x!)**: `factorial(x)`

* **Powers**: `x^n`

* **Square root**: `sqrt(x)`

* **Exponential (e^x)**: `exp(x)`

* **Logarithms**:

  ```r
  log(x) # ln(x)
  log(x, base=n) # log_n(x)
  ```

* **Absolute value**: `abs(x)`

* **Functions**:

  ```r
  f <- function(x) x^2
  f <- function(x) {
    return x^2
  }
  g <- function(x, y) x + y
  ```

* **Plot functions**:

  ```r
  x <- seq(-10, 10, 0.1) # from, to, step (default 1)
  plot(x, f(x), type="l")
  grid()
  # or
  curve(f, -10, 10)
  grid()
  # add to existing plot
  lines(x, f2(x), col="blue")
  ```

* **Sum**:

  ```r
  f <- function(x) x^2
  sum(f(1:5))
  ```

* **Integral**: `integrate(function(x) x^2, 0, 1)`

* **Derivative**: `D(expression(x^2), "x")`
