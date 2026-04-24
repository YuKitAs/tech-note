# Vectors and Matrices

* **Define a vector**:

```r
b <- c(0, 1)
```

* **Vector functions**:

```r
length(b)
mean(b) # average
var(b) # sample variance
sum(b)
prod(b)
```

* **Inspect vector elements**:

```r
# filters elements
b[b>=1]
b[b!=0]
which(b>=1) # return indices of elements
b>=1 # return TRUE or FALSE element-wise
```


* **Define a matrix**:

```r
# 1 0
# 0 1
A <- matrix(c(1, 0, 0, 1), nrow=2, ncol=2) # fills by columns by default, otherwise add `byrow=TRUE`

# 1 0 0
# 1 1 0
# 0 0 0
A <- matrix(0, 3, 3) # initialize a 3x3 matrix filled with 0
A[1,] <- c(1, 0, 0) # row 1
A[2, c(1, 2)] <- 1 # row 2, column 1, 2

# 1 0 0
# 0 1 0
# 0 0 1
diag(3)
```

* **Matrix multiplication**:

```r
A%*%B
```

* **Matrix exponentiation**:

```r
install.packages("expm")
library("expm")

A%^%2
```

* **Inverse matrix**:

```r
solve(A) # A^(-1)
solve(A, b) # solve x = A^(-1) * b i.e. Ax = b
```

* **Transpose**:

```r
t(A) # A^T
```
