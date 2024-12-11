# For Loops

Given an array:

```bash
my_array=(1 2 3 4 5)
```

Get items directly:

```bash
for item in ${my_array[@]}; do
  echo $item
done
```

Get items via indices:

```bash
for i in ${!my_array[@]}; do
  echo ${my_array[$i]}
done
```

Get items specifying iterations:

```bash
array_size = ${#my_array[@]}
for (( i = 0; i < ${array_size}; i++ )) ; do
  echo ${my_array[$i]}
done
```
