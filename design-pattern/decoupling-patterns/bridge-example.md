# Bridge example

Entkoppelt Abstraktion von ihrer Implementierung, sodass beide unabhängig voneinander variiert werden können.

_Anwendung_: Vermeidung dauerhafter Verbindung zwischen Abstraktion und ihrer Implementierung, Erweiterbarkeit sowohl von Abstraktion als auch Implementierung durch Unterklassenbildung, Nutzung einer Implementierung von mehreren Objekten aus.

![bridge](../class-diagrams/bridge.png)

**Participants:**

* Abstraction: defines the abstraction's interface; maintains a reference to an object of type Implementor.
* RefinedAbstraction: extends the interface defined by Abstraction.
* Implementor: defines the interface for implementation classes.
* ConcreteImplementor: implements the Implementor interface and defines its concrete implementation.

**Abstraction:**

  ```java
  public abstract class Shape {
    protected Color color;

    Shape(Color color) {
      this.color = color;
    }

    abstract public void applyColor();
  }
  ```
  
**RefinedAbstraction:**

  ```java
  public class Circle extends Shape {
    public Circle(Color color) {
      super(color);
    }

    @Override
    public void applyColor() {
      System.out.print("Circle is ");
      color.apply();
    }
  }
  ```
  
**Implementor:**

  ```java
  public interface Color {
    void apply();
  }
  ```
  
**ConcreteImplementorA:**

  ```java
  public class Black implements Color {
    @Override
    public void apply() {
      System.out.println("black");
    }
  }
  ```

**ConcreteImplementorB:**

  ```java
  public class White implements Color {
    @Override
    public void apply() {
      System.out.println("white");
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
        new Circle(new Black()).applyColor();
        new Circle(new White()).applyColor();
    }
  }
  ```

**Output:**

  ```
  Circle is black
  Circle is white
  ```
  
**Compared with [Adapter](https://github.com/YuKitAs/tech-note/blob/master/design-patterns/decoupling-patterns/adapter-example.md) design pattern:**

The Bridge pattern is often implemented using the Object Adapter pattern.

