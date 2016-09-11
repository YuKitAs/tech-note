# Prototype example

**Participants:**

* Prototype: declares an interface for cloning itself.
* ConcretePrototype: implements an operation for cloning itself.
* Client: creates a new object by asking a prototype to clone itself.

**Prototype:**

  ```java
  public class Shape implements Cloneable {
    private Integer id;
    protected String type;

    public void setId(Integer id) {
      this.id = id;
    }

    public Integer getId() {
      return id;
    }

    public String getType() {
      return type;
    }

    public Object clone() {
      Object clone = null;

      try {
        clone = super.clone();
      } catch (CloneNotSupportedException e) {
        e.printStackTrace();
      }

      return clone;
    }
  }
  ```
  
**ConcretePrototypeA:**

  ```java
  public class Circle extends Shape {
    public Circle() {
      type = "Circle";
    }
  }
  ```

**ConcretePrototypeB:**

  ```java
  public class Square extends Shape {
    public Square() {
      type = "Square";
    }
  }
  ```
  
**Client:**

  ```java
  import java.util.Hashtable;

  public class ShapeCache {
    private static Hashtable<Integer, Shape> shapes = new Hashtable<>();

    public static Shape getShape(Integer id) {
      Shape cachedShape = shapes.get(id);
      return (Shape) cachedShape.clone();
    }

    public static void loadCache() {
      Circle circle = new Circle();
      circle.setId(1);
      shapes.put(circle.getId(), circle);

      Square square = new Square();
      square.setId(2);
      shapes.put(square.getId(), square);
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      ShapeCache.loadCache();

      Shape clonedShape1 = ShapeCache.getShape(1);
      System.out.println("Shape: " + clonedShape1.getType());

      Shape clonedShape2 = ShapeCache.getShape(2);
      System.out.println("Shape: " + clonedShape2.getType());
    }
  }
  ```
  
**Output:**

  ```
  Shape1: Circle
  Shape2: Square
  ```