# Annotations

Annotations can be applied to declarations of different program elements (e.g. classes, methods, fields, constructors) and uses of types (since Java 8, e.g. `@NonNull String str`). Some are used by the Java compiler to detect errors or suppress warnings, some are processed by a tool or framework to generate code, files, etc., and some are processed at runtime.

There is a set of [predefined annotation types](https://docs.oracle.com/javase/tutorial/java/annotations/predefined.html) in Java. While `@Deprecated`, `@Override`, `@SuppressWarnings`, `@SafeVarargs` and `@FunctionalInterface` are used by the compiler, `@Retention`, `@Documented`, `@Target`, `@Inherited` and `@Repeatable` are applied to declarations of other annotations and are called meta-annotations.

The following example shows how to declare an annotation type:

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface MyAnnotation {
    String name();
    int value() default 0;
}
```

The `@Retention(RetentionPolicy.RUNTIME)` annotation indicates the annotation should be processed at runtime, the `@Target(ElementType.METHOD)` restricts the annotation can only be applied to methods. Annotation types are a form of interface so they should be declared with `@interface`. This annotation can then be used like `@MyAnnotation(name = "Bonbon")` or `@MyAnnotation(name = "Bonbon", value = 42)` with some information on method declarations. And in programs that need to deal with this kind of annotations, we can use `isAnnotationPresent(MyAnnotation.class)` to check the annotated methods.
