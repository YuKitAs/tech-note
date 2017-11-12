# Composite example

Fügt Objekte zu Baumstrukturen zusammen, um Hierarchien zu repräsentieren. Einheitliche Behandlung von Objekten wie Aggregaten.

![composite](../class-diagrams/composite.png)

**Participants:**

* Component: declares the interface for objects in the composition; implements default behavior for the interface common to all classes; child object of composite.
* Leaf: represents leaf objects in the composition; defines behavior for primitive objects in the composition.
* Composite: defines behavior for components having children; stores child components; implements child-related operations in the Component interface.
* Client: manipulates objects in the composition through the Component interface.

**Component:**

  ```java
  public abstract class Employee {
      abstract void add(Employee employee);

      abstract String getName();

      abstract String getEntryYear();

      // common operation
      void print() {
          System.out.println("Name: " + getName() + ", Year of Entry: " + getEntryYear());
      }
  }
  ```

**Leaf:**

  ```java
  public class Developer extends Employee {
      private final String name;
      private final String entryYear;

      public Developer(String name, String entryYear) {
          this.name = name;
          this.entryYear = entryYear;
      }

      @Override
      public void add(Employee employee) {
          // a leaf has no children
      }

      @Override
      public String getName() {
          return name;
      }

      @Override
      public String getEntryYear() {
          return entryYear;
      }
  }
  ```

**Composite:**

  ```java
  public class Manager extends Employee {
      private final String name;
      private final String entryYear;
      private List<Employee> employees;

      public Manager(String name, String entryYear) {
          this.name = name;
          this.entryYear = entryYear;
          employees = new ArrayList<>();
      }

      @Override
      public void add(Employee employee) {
          employees.add(employee);
      }

      @Override
      public String getName() {
          return name;
      }

      @Override
      public String getEntryYear() {
          return entryYear;
      }

      @Override
      public void print() {
          System.out.println("Name: " + getName() + ", Year of Entry: " + getEntryYear());

          // use iterator in composite to execute the common operation of the children.
          Iterator<Employee> employeeIterator = employees.iterator();
          while (employeeIterator.hasNext()) {
              employeeIterator.next().print();
          }
      }
  }
  ```

**Demo:**

  ```java
  public class Main {
      public static void main(String[] args) {
          Employee generalManager = new Manager("Michael", "2004");
          Employee manager = new Manager("Phillip", "2006");
          Employee developer1 = new Developer("Peter", "2012");
          Employee developer2 = new Developer("Angela", "2014");
          Employee developer3 = new Developer("Johan", "2016");

          generalManager.add(manager);
          generalManager.add(developer1);
          manager.add(developer2);
          manager.add(developer3);

          generalManager.print();
    }
  }
  ```

The actual hierarchical structure is defined as follows:

  ```
        Michael
        /     \
    Phillip  Peter
    /    \
 Angela Johan
  ```

**Output:**

  ```
  Name: Michael, Year of Entry: 2004
  Name: Phillip, Year of Entry: 2006
  Name: Angela, Year of Entry: 2014
  Name: Johan, Year of Entry: 2016
  Name: Peter, Year of Entry: 2012
  ```
