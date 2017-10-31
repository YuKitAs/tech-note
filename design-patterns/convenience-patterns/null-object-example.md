# Null Object example

Stellvertreter eines Objekts mit gleicher Schnittstelle, der nichts tut. Vermeidet unnötige null-Prüfungen.

**Participants:**

* AbstractObject: specifies various operations to be done.
* RealObject: extends the abstract class.
* NullObject: provides do-nothing implementation of the abstract class.

**AbstractObject:**

  ```java
  public abstract class User {
      protected String name;

      public abstract String getName();

      public abstract boolean isNull();
  }
  ```

**RealObject:**

  ```java
  public class RealUser extends User {
      public RealUser(String name) {
          this.name = name;
      }

      @Override
      public String getName() {
          return name;
      }

      @Override
      public boolean isNull() {
          return false;
      }
  }
  ```

**NullObject:**

  ```java
  public class NullUser extends User {
      @Override
      public String getName() {
          return "Phantom";
      }

      @Override
      public boolean isNull() {
          return true;
      }
  }
  ```

**Demo:**

  ```java
  public class UserNameBook {
      private static final String[] names = {"Anton", "Berta", "Charlotte"};

      public static User getUser(String name) {
          if (Arrays.asList(names).contains(name)) {
              return new RealUser(name);
          }

          return new NullUser();
      }
  }
  ```

  ```java
  public class Main {
      public static void main(String[] args) {
          User user1 = UserNameBook.getUser("Anton");
          User user2 = UserNameBook.getUser("Berta");
          User user3 = UserNameBook.getUser("Charlotte");
          User user4 = UserNameBook.getUser("Mimikyu");

          System.out.println(user1.getName());
          System.out.println(user2.getName());
          System.out.println(user3.getName());
          System.out.println(user4.getName());
      }
  }
  ```

**Output:**

  ```
  Anton
  Berta
  Charlotte
  Phantom
  ```
