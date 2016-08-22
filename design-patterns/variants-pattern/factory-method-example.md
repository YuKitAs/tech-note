# Factory Method example

**Participants:**

* Product: defines the interface of objects the factory method creates.
* ConcreteProduct: implements the Product interface.
* Creator: declares the factory method; may call the factory method to create a Product object.
* ConcreteCreator: overrides the factory method to return an instance of a ConcreteProduct.

**Product:**

  ```java
  public interface Shape {
    void draw();
  }
  ```
  
**ConcreteProductA:**

  ```java
  public class Circle implements Shape {
    @Override
    public void draw() {
      System.out.println("This is a circle.");
    }
  }
  ```
  
**ConcreteProductB:**

  ```java
  public class Square implements Shape {
    @Override
    public void draw() {
      System.out.println("This is a square.");
    }
  }
  ```
  
**ConcreteCreator:**

  ```java
  public class ShapeFactory {
    public Shape getShape(String shape) {
      if (shape.equalsIgnoreCase("CIRCLE")) {
        return new Circle();
      } else if (shape.equalsIgnoreCase("SQUARE")) {
        return new Square();
      }

      return null;
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();

      Shape shape1 = shapeFactory.getShape("circle");
      shape1.draw();

      Shape shape2 = shapeFactory.getShape("square");
      shape2.draw();
    }
  }
  ```
  
**Output:**

  ```
  This is a circle.
  This is a square.
  ```
  
**Compared with Abstract Factory design pattern:**

Abstract Factory is often implemented with Factory Methods.