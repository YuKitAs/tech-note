# File Cache Conflict When Running Jetty

When Jetty is running and one tries to make some local changes, WebStorm would keep warning `File Cache Conflict`, to solve this problem, open `path/to/jetty/etc/webdefault.xml`, find the following parameter

```xml
<init-param>
    <param-name>useFileMappedBuffer</param-name>
    <param-value>true</param-value>
</init-param>
```

and change the parameter value to `false`.