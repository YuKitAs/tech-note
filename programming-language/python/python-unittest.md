# Python Unittest


For a simple method in `main.py`:

```python
def sum(a):
    s = 0
    for i in a:
        s += i
    return s
```

In the test script `main_test.py`, import the build-in `unittest` library and the script to test:

```python
import unittest

import main
```

Create a test class and specify the entry point:

```python
class MainTest(unittest.TestCase):

    def test_sum_int_list(self):
        self.assertEqual(main.sum([1, 2, 3, 4]), 10, "Should be 10")

    def test_sum_float_list(self):
        self.assertEqual(main.sum([1.1, 2.2, 3.3]), 6.6, "Should be 6.6")

    def test_sum_int_set(self):
        self.assertEqual(main.sum({1, 2, 3}), 6, "Should be 6")

    def test_sum_string_list(self):
        with self.assertRaises(TypeError):
            main.sum(['a', 'b'])


if __name__ == '__main__':
    unittest.main()
```

Execute tests:

```console
$ python -m unittest main_test
```
