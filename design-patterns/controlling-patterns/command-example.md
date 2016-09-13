# Command example

**Participants:**

* Command: declares an interface for executing an operation.
* ConcreteCommand: defines a binding between a Receiver object and an action; implements Execute by invoking the corresponding operation(s) on Receiver.
* Client: creates a ConcreteCommand object and sets its receiver.
* Invoker: asks the command to carry out the request.
* Receiver: knows how to perform the operations associated with carrying out a request.

**Command:**

  ```java
  public abstract class Order {
    protected Item quafe;

    public Order(Item quafe) {
      this.quafe = quafe;
    }

    abstract void execute();
  }
  ```
  
**ConcreteCommandA:**

  ```java
  public class BuyItem extends Order {
    public BuyItem(Item quafe) {
      super(quafe);
    }

    @Override
    public void execute() {
      quafe.buy();
    }
  }
  ```
  
**ConcreteCommandB:**

  ```java
  public class SellItem extends Order {
    public SellItem(Item quafe) {
      super(quafe);
    }

    @Override
    public void execute() {
      quafe.sell();
    }
  }
  ```
  
**Invoker:**

  ```java
  public class Item {
    private String name = "Quafe";
    private int quantity = 100;

    public void buy() {
      System.out.println("Item [Name: " + name + ", Quantity: " + quantity + "] bought.");
    }

    public void sell() {
      System.out.println("Item [Name: " + name + ", Quantity: " + quantity + "] sold.");
    }
  }

  ```
  
**Receiver:**

  ```java
  import java.util.ArrayList;
  import java.util.List;

  public class Player {
    private List<Order> orderList = new ArrayList<>();

    public void takeOrder(Order order) {
      orderList.add(order);
    }

    public void placeOrders() {
      orderList.forEach(order -> order.execute());
      orderList.clear();
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      Item quafe = new Item();

      BuyItem buyItemOrder = new BuyItem(quafe);
      SellItem sellItemOrder = new SellItem(quafe);

      Player player = new Player();
      player.takeOrder(buyItemOrder);
      player.takeOrder(sellItemOrder);

      player.placeOrders();
    }
  }
  ```
  
**Output:**

  ```
  Item [Name: Quafe, Quantity: 100] bought.
  Item [Name: Quafe, Quantity: 100] sold.
  ```