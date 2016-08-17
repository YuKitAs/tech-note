# Mediator example

**Participants:**

* Mediator: defines an interface for communicating with Colleague objects.
* ConcreteMediator: implements cooperative behavior by coordinating Colleague objects; knows and maintains its colleagues.
* Colleague: each Colleague knows its Mediator object.

**Mediator:**

  ```java
  public interface Mediator {
    void showMessage(Colleague colleague, String message);
  }
  ```
  
**ConcreteMediator:**

  ```java
  public class MessageMediator implements Mediator {
    @Override
    public void showMessage(Colleague colleague, String message) {
      System.out.println("[" + colleague.getName() + "]: " + message);
    }
  }
  ```
  
**Colleague:**

  ```java
  public abstract class Colleague {
    protected Mediator mediator;

    public Colleague(Mediator mediator) {
      this.mediator = mediator;
    }

    public abstract void sendMessage();

    public abstract String getName();
  }
  ```
  
**ConcreteColleagueA:**

  ```java
  public class ColleagueA extends Colleague {
    public ColleagueA(Mediator mediator) {
      super(mediator);
    }

    @Override
    public void sendMessage() {
      mediator.showMessage(this, "Hello World!");
    }
    
    @Override
    public String getName() {
      return "A";
    }
  }
  ```
  
**ConcreteColleagueB:**

  ```java
  public class ColleagueB extends Colleague {
    public ColleagueB(Mediator mediator) {
      super(mediator);
    }

    @Override
    public void sendMessage() {
      mediator.showMessage(this, "Goodbye World!");
    }

    @Override
    public String getName() {
      return "B";
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      Mediator mediator = new MessageMediator();
      Colleague colleagueA = new ColleagueA("A", mediator);
      Colleague colleagueB = new ColleagueB("B", mediator);

      colleagueA.sendMessage();
      colleagueB.sendMessage();
    }
  }
  ```
  
**Output:**

  ```
  [A]: Hello World!
  [B]: Goodbye World!
  ```