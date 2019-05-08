# Clean APT Cache

The cached package files generated from `apt install` are located in `/var/cache/apt/archives`.

`sudo apt autoclean` will remove the package files that can no longer be downloaded from the sources.

`sudo apt clean` will remove the files from `/var/cache/apt/archives` except the `partial` folder and the `lock` file.

The state information for each package resource is stored in `/var/lib/apt/lists`. The files there will be re-generated from every `apt update`.

All these files can be removed with:

```console
# rm -rf /var/lib/apt/lists/* /var/cache/apt/*
```
