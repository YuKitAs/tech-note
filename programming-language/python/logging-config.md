# Logging Config

Import the `logging` module:

```python
import logging
```

## Global config

* Configure logging format:

  ```python
  logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
  ```

* Format timestamp:

  ```python
  logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m-%d %H:%M')
  ```

* Log to external file:

  ```python
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      filename='app.log',
                      filemode='w',
                      level='INFO')
  ```

The default file mode is `a` (append). The default logging level is `WARNING`.
  
  
## Logger config

* Define logger:

  ```python
  logger = logging.getLogger('myapp')
  ```
  
* Set logging level:

  ```python
  logger.setLevel(logging.DEBUG)
  ```

* Logging example:

  ```python
  logging.info('Jackdaws love my big sphinx of quartz.') # root logger
  logger.warning('Jail zesty vixen who grabbed pay from quack.')
  ```

  Output:

  ```
  2019-09-15 23:00:00,437 - root - INFO - Jackdaws love my big sphinx of quartz.
  2019-09-15 23:00:00,438 - myapp - WARNING - Jail zesty vixen who grabbed pay from quack.
  ```

## Reference

* [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#formatting-styles)
