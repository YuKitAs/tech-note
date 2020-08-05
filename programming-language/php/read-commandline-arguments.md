# Read Command-line Arguments

## Read arguments as array

Example:
```php
var_dump($argv[1]);
```

Test:
```console
php script.php arg1
```

Output:
```
string(4) "arg1"
```

## Parse options

Options: a character (`a-zA-Z0-9`) starting with `-`.

Long options: a string starting with `--`.

Example:
```php
$shortopts = "f:v::a"; // value required: -f; value optional: -v; no value: -a
$longopts = array(
  "required:", "optional::", "opt"
);
var_dump(getopt($shortopts, $longopts));
```

Test:
```console
php script.php -f foo -v -a --required value --optional=bar --opt
```

Example:
```php
array(6) {
  ["f"]=>
  string(3) "foo"
  ["v"]=>
  bool(false)
  ["a"]=>
  bool(false)
  ["required"]=>
  string(5) "value"
  ["optional"]=>
  string(3) "bar"
  ["opt"]=>
  bool(false)
}
```

## Read input interactively

Example:
```php
echo "Username: ";
var_dump(trim(fgets(STDIN)));
```

Output:
```
Username: foo
string(3) "foo"
```

Enter input securely (invisible) by disabling `echo`:

```php
echo "Password: ";
system('stty -echo');
$password = trim(fgets(STDIN));
system('stty echo');
```
