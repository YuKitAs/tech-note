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
  # generate random samples from normal distribution
  x <- rnorm(n, mean=mu, sd=sigma) # defaults: mean=0, sd=1

  # P(X <= a) = P(X < a) (P(X = a) = 0)
  pnorm(a, mean=mu, sd=sigma)
  # equivalent to
  pnorm((a - mu) / sigma)

  # P(X_mean <= a) for X_mean ~ N(mu, sigma^2/n)
  pnorm(a, mean=mu, sd=sigma / sqrt(n))
  pnorm((a - mu) / (sigma / sqrt(n)))

  # P(a <= X <= b)
  pnorm(b, mean=mu, sd=sigma) - pnorm(a, mean=mu, sd=sigma)

  # find x for P(X <= x) = p = (conf.level + 1) / 2
  qnorm(p, mean=mu, sd=sigma)
  ```

* **Chi-square distribution**:

  ```r
  # generate random samples from chi-square distribution
  x <- rchisq(n, df) # df: degree of freedom

  # find x for P(X <= x) = p
  qchisq(p, df)
  ```

* **t distribution**:

  ```r
  # generate random samples from t distribution
  x <- rt(n, df)

  # find x for P(X <= x) = p = (conf.level + 1) / 2
  qt(p, df)
  ```

* **Gamma distribution**:

  ```r
  # generate random samples from gamma distribution
  x <- rgamma(n, shape=alpha, rate=beta)

  # P(X <= a)
  pgamma(a, shape=alpha, rate=beta)

  # find x for P(X <= x) = p = (conf.level + 1) / 2
  qgamma(p, shape=alpha, rate=beta)
  ```
