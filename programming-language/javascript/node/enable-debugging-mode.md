# Enable Debugging Mode

To start a Node.js app in debugging mode, add the `--inspect` flag like:

```console
$ node --inspect <app>
```

To enable the debugging mode of a running Node.js app without restarting it, we can send `SIGUSR1` (user-defined signal 1) to the process of the running app like:

```console
$ kill -SIGUSR1 <PID>
```

Once the app is running in debugging/inspect mode, we can use Chrome DevTools (enter `chrome://inspect`) or VS Code to connect a debugger to the running process.
