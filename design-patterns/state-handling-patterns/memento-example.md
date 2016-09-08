# Memento example

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

    public Memento saveStateToMemento() {
      return new Memento(state);
    }

    public void loadStateFromMemento(Memento memento) {
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

    public List<Memento> getAllMementos() {
      return mementos;
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

      originator.setState("State #1");
      careTaker.add(originator.saveStateToMemento());

      originator.setState("State #2");
      careTaker.add(originator.saveStateToMemento());

      originator.setState("State #3");
      System.out.println("Current state: " + originator.getState());

      careTaker.getAllMementos().forEach(memo -> {
        originator.loadStateFromMemento(memo);
        System.out.println("Saved state: " + originator.getState());
      });
    }
  }
  ```
  
**Output:**

  ```java
  Current state: State #3
  Saved state: State #1
  Saved state: State #2
  ```