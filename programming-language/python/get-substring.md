# Get Substring

A substring can be got with the help of the slice notation.

* Start from the third character:
```python
>>> print("Hello world!"[2:])
llo world!
```

* Stop at the third character (keep the first two characters):
```python
>>> print("Hello world!"[:2])
He
```

* Start from the third character from the right side (keep the last two characters):
```python
>>> print("Hello world!"[-2:])
d!
```

* Stop at the third character from the right side (drop the last two characters):
```python
>>> print("Hello world!"[:-2])
Hello worl
```

* Start from the third character and stop at the third character from the right side:
```python
>>> print("Hello world!"[2:-2])
llo worl
```
