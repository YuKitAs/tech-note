# Observer example

Participants:

* Subject: knows its observers; provides an interface for attaching and detaching Observer objects.
* Observer: defines an updating interface for objects that should be notified of changes in a subject.
* ConcreteSubject: stores states of interest to ConcreteObserver objects; sends a notification to its observers when its state changes.
* ConcreteObserver: maintains a reference to a ConcreteSubject object; stores state that should stay consistent with the subject's; implements the Observer updating interface to keep its state consistent with the subject's.

Subject:

  ```java
  public interface Observable {
    public int getValue();

    public void setValue(int value);

    public void attach(Observer ob);

    public void detach(Observer ob);

    public void notifyObservers();
  }
  ```
  
Observer:

  ```java
  public interface Observer {
    public void update();
  }
  ```
  
ConcreteSubject:

  ```java
  public class ObservableValue implements Observable {
    private List<Observer> obs = new ArrayList<Observer>();
    private int value;

    @Override
    public int getValue() {
      return value;
    }

    @Override
    public void setValue(int value) {
      this.value = value;
      notifyObservers();
    }

    @Override
    public void attach(Observer ob) {
      obs.add(ob);
    }

    @Override
    public void detach(Observer ob) {
      obs.remove(ob);
    }

    @Override
    public void notifyObservers() {
      for (Observer ob : obs) {
        ob.update();
      }
    }
  }
  ```

ConcreteObserver:

  ```java
  public class ValueObserver implements Observer {
    private Observable observable;

    public ValueObserver(Observable observable) {
      this.observable = observable;
      this.observable.attach(this);
    }

    @Override
    public void update() {
      System.out.println("Observed value: " + observable.getValue());
    }
  }
  ```
  
How it works:

  ```java
  public class Main {
    public static void main(String[] args) {
      Observable observable = new ObservableValue();
      new ValueObserver(observable);
      observable.setValue(60);
      observable.setValue(100);
    }
  }
  ```

Output:

Observed value: 60

Observed value: 100
