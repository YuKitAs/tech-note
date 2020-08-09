# Java Console

If any character-based console device is associated with the current JVM, it can be accessed like this:

```java
Console c = System.console();
if (c == null) {
    System.err.println("No console.");
    System.exit(1);
}

String login = c.readLine("Enter your login: ");
char[] password = c.readPassword("Enter your password: ");
```
