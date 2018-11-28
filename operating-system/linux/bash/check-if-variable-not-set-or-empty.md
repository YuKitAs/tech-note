# Check If Variable Not Set or Empty

```bash
# $VAR is not set or empty
if [ -z $VAR ]; then
  echo "\$VAR not set"
fi

# $VAR is set or non-empty
if [ -n $VAR ]; then
  echo $VAR
fi
```
