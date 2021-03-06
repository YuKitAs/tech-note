# Memento example

Externalisiert eine Momentaufnahme des internen Zustands eines Objekts (ohne die Implementierungsdetails offenzulegen), sodass das Objekt später in diesen Zustand zurückversetzt werden kann.

_Beispiel_: Speicherung von Spielständen

![memento](../class-diagrams/memento.png)

**Participants:**

* Memento: stores internal state of the Originator object; protects against access by objects other than the originator.
* Originator: creates a memento containing a snapshot of its current internal state; uses the memento to restore its internal state.
* Caretaker: responsible for the memento's safekeeping.

**Memento:**

  ```java
  public class Memento {
    private String state;

    public Memento(String state) {
      this.state = state;
    }

    public String getState() {
      return state;
    }
  }
  ```
  
**Originator:**

  ```java
  public class Originator {
    private String state;

    public void setState(String state) {
      this.state = state;
    }

    public String getState() {
      return state;
    }

    public Memento saveState() {
      return new Memento(state);
    }

    public void restoreState(Memento memento) {
      state = memento.getState();
    }
  }
  ```
  
**Caretaker:**

  ```java
  import java.util.ArrayList;
  import java.util.List;

  public class CareTaker {
    private List<Memento> mementos = new ArrayList<>();

    public void add(Memento memento) {
      mementos.add(memento);
    }

    public Memento get(int i) {
      return mementos.get(i);
    }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      Originator originator = new Originator();
      CareTaker careTaker = new CareTaker();

      originator.setState("State1");

      originator.setState("State2");
      careTaker.add(originator.saveState());

      originator.setState("State3");
      System.out.println("Current state: " + originator.getState());

      originator.restoreState(careTaker.get(0));
      System.out.println("First saved state: " + originator.getState());
    }
  }
  ```
  
**Output:**

  ```java
  Current state: State3
  First saved state: State2
  ```
