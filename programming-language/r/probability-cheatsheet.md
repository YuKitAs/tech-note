# Probability Cheatsheet

* **Choose k from n (unordered)**:

  ```r
  choose(n, k) # equivalent to factorial(n) / (factorial(k) * factorial(n - k))
  ```

* **Binomial distribution**:

  ```r
  # P(X = k)
  dbinom(k, size=n, prob=p)
  # P(X <= k)
  pbinom(k, size=n, prob=p)
  # P(X >= k) = 1 - P(X <= k - 1)
  pbinom(k - 1, size=n, prob=p)
  sum(dbinom(k:n, size=n, prob=p))
  ```

* **Poisson distribution**:

  ```r
  # P(X = k)
  dpois(k, lambda)
  # P(X <= k)
  ppois(k, lambda)
  ```

* **Exponential distribution**:

  ```r
  # P(X <= k)
  pexp(k, rate=lambda)
  ```

* **Normal distribution**:

  ```r
  # P(X <= a) = P(X < a) (for sample mean)
  pnorm(a, mean=mu, sd=sigma/sqrt(n))
  pnorm((a - mu) / (sigma / sqrt(n)))
  # P(a <= X <= b)
  pnorm(b, mean=mu, sd=sigma) - pnorm(a, mean=mu, sd=sigma)
  # find x for P(X <= x) = a
  qnorm(a, mean=mu, sd=sigma)
  ```

* **Gamma distribution**:

  ```r
  # P(X <= x) = p = (conf.level + 1) / 2
  qgamma((conf.level + 1) / 2, shape=alpha, rate=beta)
  ```
