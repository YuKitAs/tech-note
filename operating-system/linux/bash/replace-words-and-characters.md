# Replace Words and Characters

* Replacing words in text with `sed`:

  ```console
  $ echo "Hello world" | sed 's/Hello/Goodbye/'
  Goodbye world
  ```

* Removing words in text with `sed`:

  ```console
  $ echo "Hello world" | sed 's/ world//'
  Hello
  ```

* Replacing characters in text with `tr`:

  ```console
  $ echo "Hello world" | tr l 1
  He11o wor1d
  $ echo "Hello world" | tr '[:lower:]' '[:upper:]'
  HELLO WORLD
  ```

* Removing non-alphanumeric characters in text with `tr`:

  ```console
  $ echo 'Hello $world!' | tr -dc '[:alnum:]'
  Helloworld
  ```
