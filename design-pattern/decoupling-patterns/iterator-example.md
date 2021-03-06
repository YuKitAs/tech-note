# Iterator example

Ermöglicht den sequentiellen Zugriff auf Elemente eines zusammengesetzten Objekts, ohne die interne Repräsentation offenzulegen und bietet eine einheitliche Schnittstelle zur Traversierung unterschiedlichen Strukturen (polymorphe Iteration).

Iterator ist robust, d.h. jeder Iterator enthält eine eigene "Laufvariable".

![iterator](../class-diagrams/iterator.png)

**Participants:**

* Iterator: defines an interface for accessing and traversing elements.
* ConcreteIterator: implements Iterator; keeps track of the current position in the traversal of the aggregate.
* Aggregate: defines an interface for creating an Iterator object.
* ConcreteAggregate: implements the Iterator creation interface to return an instance of the proper ConcreteIterator.

**Iterator:**

  ```java
  public interface Iterator {
    boolean hasNext();
    String next();
  }
  ```
  
**Aggregate:**

  ```java
  public interface Repo {
    Iterator getIterator();
  }
  ```
  
**ConcreteAggregate with ConcreteIterator:**

  ```java
  public class NameRepo implements Repo {
    public String[] names = {"Alvin", "Simon", "Theodore"};

    @Override
    public Iterator getIterator() {
      return new NameIterator();
    }

    private class NameIterator implements Iterator {
      int i; // will be initialized to default value 0 as class member variable

      @Override
      public boolean hasNext() {
        return i < names.length;
      }

      @Override
      public String next() {
        if (!this.hasNext()) return null;
            
        return names[i++];
      }
    }
  }
  ```

**Demo:**

  ```java
  public class Main {
    public static void main(String[] args) {
      NameRepo nameRepo = new NameRepo();

      for (Iterator iter = nameRepo.getIterator(); iter.hasNext(); ) {
        System.out.println("Name: " + iter.next());
      }
    }
  }
  ```

**Output:**

  ```
  Name: Alvin
  Name: Simon
  Name: Theodore
  ```
