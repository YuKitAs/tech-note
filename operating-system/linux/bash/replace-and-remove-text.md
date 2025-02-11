# Replace and Remove Text

## With `sed`

* Replace all occurrence of a pattern (`g` means globally, without `g` only the first occurrence will be replaced):

  ```console
  $ sed 's/pattern/new_pattern/g' <file>
  ```

  **Examples**

  * Replace words in text:

    ```console
    $ echo "Hello world!" | sed 's/Hello/Goodbye/'
    Goodbye world
    ```

  * Remove words in text:

    ```console
    $ echo "Hello world" | sed 's/ world//'
    Hello
    ```

* Delete line(s) matching pattern:

  ```console
  $ sed '/pattern/d' <file>
  ```

  **Examples**

  * Delete the n-th line:

    ```console
    $ sed 'nd' <file>
    ```

  * Delete the last line:

    ```console
    $ sed '$d' <file>
    ```

  * Delete lines from x to y (inclusive):

    ```console
    $ sed 'x,yd' <file>
    ```

* Remove a directory `/home/wrong/bin` from `PATH`:

  ```console
  $ export PATH=`echo $PATH | sed -e 's/:\/home\/wrong\/bin//'`
  ```

## With `tr`

* Replace characters in text:

  ```console
  $ echo "Hello world" | tr l 1
  He11o wor1d
  $ echo "Hello world" | tr '[:lower:]' '[:upper:]'
  HELLO WORLD
  ```

* Remove non-alphanumeric characters in text:

  ```console
  $ echo 'Hello $world!' | tr -dc '[:alnum:]'
  Helloworld
  ```
