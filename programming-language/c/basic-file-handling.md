# Basic File Handling

## Get file size

Using [`stat`](https://linux.die.net/man/2/stat):

```c
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>

size_t get_file_size(const char *path) {
  struct stat file_info;
  stat(path, &file_info);
  return file_info.st_size;
}
```

## Open and read from file

Using `fopen` and `fscanf`:

```c
FILE *fp;
fp = fopen(path, "r");
// read the first two strings
char str1[10], str2[10];
fscanf(fp, "%s %s", str1, str2);
```

Using `open`:

```c
int fd = open(path, O_RDONLY);
```

## Write to file

Using `fopen` and `fputs` or `fprintf`:

```c
FILE *fp;
fp = fopen(path, "w");

fputs("Hello world", fp);
// or formatted output
fprintf(fp, "%s %s", "Hello", "world");
```

## Close a file

Using `fclose`:

```c
fclose(fp);
```

Using `close`:

```c
close(fd);
```
