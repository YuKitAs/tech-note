# Build Jar with Dependencies

Add the following plugin to `pom.xml`:

```xml
<plugin>
  <artifactId>maven-assembly-plugin</artifactId>
  <executions>
    <execution>
      <phase>package</phase>
      <goals>
        <goal>single</goal>
      </goals>
    </execution>
  </executions>
  <configuration>
    <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
    </descriptorRefs>
    <archive>
      <manifest>
        <addClasspath>true</addClasspath>
        <mainClass>${package.to.mainClass}</mainClass>
      </manifest>
    </archive>
  </configuration>
</plugin>
```
