# Facade example

Bietet eine einheitliche Schnittstelle zu einer Menge von Schnittstellen eines Subsystems. Vereinfacht die Benutzung eines komplexen Subsystems und entkoppelt das Subsystem von den Klienten und anderen Subsystemen.

**Participants:**

* Facade: knows which Subsystem classes are responsible for a request; delegates client request to appropriate Subsystem objects.
* Subsystem classes: implements Subsystem functionality; handle work assigned by the Facade object.

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
          System.out.println("Drawing circle...");
      }
  }
  ```

  ```java
  public class Square implements Shape {
      @Override
      public void draw() {
          System.out.println("Drawing square...");
      }
  }
  ```

**Facade:**

  ```java
  public class ShapeDrawer {
      private Shape circle;
      private Shape square;

      public ShapeDrawer() {
          circle = new Circle();
          square = new Square();
      }

      public void drawCircle() {
          circle.draw();
      }

      public void drawSquare() {
          square.draw();
      }
  }
  ```

**Demo:**

  ```java
  public class Main {
      public static void main(String[] args) {
          ShapeDrawer shapeDrawer = new ShapeDrawer();

          shapeDrawer.drawCircle();
          shapeDrawer.drawSquare();
      }
  }
  ```

**Output:**

  ```
  Drawing circle...
  Drawing square...
  ```
