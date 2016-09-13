# Command example

**Participants:**

* Command: declares an interface for executing an operation.
* ConcreteCommand: defines a binding between a Receiver object and an action; implements execute() method by invoking the corresponding operation(s) on Receiver.
* Client: creates a ConcreteCommand object and sets its receiver.
* Invoker: asks the Command to carry out the request by calling its execute() method.
* Receiver: knows how to perform the operations needed to carry out a request; any class can act as a Receiver.

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
  
**Receiver:**

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