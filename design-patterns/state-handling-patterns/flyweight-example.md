# Flyweight example

![flyweight](../class-diagrams/flyweight.png)

**Participants:**

* Flyweight: declares an interface through which flyweights can receive and act on extrinsic state.
* ConcreteFlyweight: implements the Flyweight interface and adds storage for intrinsic state, if any. A ConcreteFlyweight object must be sharable.
* UnsharedConcreteFlyweight: may have ConcreteFlyweight objects as children at some level.
* FlyweightFactory: creates and manages flyweight objects; ensures that flyweights are shared properly.

**Flyweight:**

  ```java
  public interface Shape {
    void draw();
  }
  ```
  
**ConcreteFlyweight:**

  ```java
  public class Circle implements Shape {
    private int x;

    private int y;

    private int radius;

    public Circle() {
    }

    public void setX(int x) {
      this.x = x;
    }

    public void setY(int y) {
      this.y = y;
    }

    public void setRadius(int radius) {
      this.radius = radius;
    }

    @Override
    public void draw() {
      System.out.println("x: " + x + ", y: " + y);
      System.out.println("radius: " + radius);
    }
  }
  ```
  
**FlyweightFactory:**

  ```java
  import java.util.ArrayList;
  import java.util.HashMap;
  import java.util.List;

  public class ShapeFactory {
    public static Shape getCircle() {
      System.out.println("Drawing circle...");

      return new Circle();
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      for (int i = 0; i < 5; i++) {
        Circle circle = (Circle) ShapeFactory.getCircle();
        
        circle.setX((int) (Math.random() * 100));
        circle.setY((int) (Math.random() * 100));
        circle.setRadius((int) (Math.random() * 100 + 1));
        
        circle.draw();
      }
    }
  }
  ```
  
**Output:**

  ```
  Drawing circle...
  x: 30, y: 21
  radius: 59
  Drawing circle...
  x: 53, y: 55
  radius: 58
  Drawing circle...
  x: 1, y: 81
  radius: 63
  Drawing circle...
  x: 0, y: 62
  radius: 3
  Drawing circle...
  x: 43, y: 38
  radius: 70
  ```