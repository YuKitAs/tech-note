# Facade example

**Participants:**

* Facade: knows which Subsystem classes are responsible for a request; delegates client request to appropriate Subsystem objects.
* Subsystem classes: implements Subsystem functionality; handle work assigned by the Facade object.

**Facade:**

  ```java
  public class ShapeDrawer {
    private Shape circle;

    public ShapeDrawer() {
      circle = new Circle();
    }

    public void drawCircle() {
      circle.draw();
    }
  }
  ```
  
**Subsystem classes:**

  ```java
  public interface Shape {
    void draw();
  }
  ```
  
  ```java
  public class Circle implements Shape {
    @Override
    public void draw() {
      System.out.println("This is a circle.");
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      ShapeDrawer shapeDrawer = new ShapeDrawer();

      shapeDrawer.drawCircle();
    }
  }
  ```
  
**Output:**

  ```
  This is a circle.
  ```