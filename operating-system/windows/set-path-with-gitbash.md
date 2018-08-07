# Set Path with GitBash

Theoretically GitBash will import all the environment variables set on Windows. But somehow I don't like this way. As I'm always working with GitBash on Windows, I want to set env variables permanently with GitBash. In the Windows world, I need to create a `.bash_profile` under the directory `C:\users\<userName>` with env variables normally like:

```bash
# An example from Internet
export JAVA_HOME='/c/Programme/Java/jdk1.8.0_45' # Here I prefer to use the German name to get rid of the white space issue
export PATH=$JAVA_HOME/bin:$PATH
```

Restart GitBash and check `echo $PATH`.
