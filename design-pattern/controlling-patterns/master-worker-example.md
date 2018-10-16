# Master/Worker example

Auftraggeber verteilt Arbeit an identische Arbeiter (Auftragnehmer) und berechnet das Endergebnis aus den zurückgelieferten Teilergebnissen.

_Zweck_: Teile & Herrsche, Parallelisierung

**Participants:**

* Master: responsible for creating and launching active Worker objects.
* Worker: extends Java's `Thread` class and override its `run` method.

**Master:**

  ```java
  public class Master {
      private static final int WORKER_COUNT = 5;
      private Worker[] workers = new Worker[WORKER_COUNT];

      public void run() {
          for (int i = 0; i < WORKER_COUNT; i++) {
              workers[i] = new Worker();
          }

          Arrays.stream(workers).forEach(worker -> worker.start());

          Arrays.stream(workers).forEach(worker -> {
              try {
                  worker.join();
              } catch (InterruptedException e) {
                  e.printStackTrace();
              } finally {
                  System.out.println(worker.getName() + " has died.");
              }
          });

          System.out.println("The master will now die...");
      }
  }
  ```
  
**Worker:**

  ```java
  public class Worker extends Thread {
      private Boolean done = false;

      public void halt() {
          done = true;
      }

      protected Boolean task() {
          return true;
      }

      public void run() {
          while (!done) {
              done = task();
          }

          try {
              Thread.sleep(1000);
          } catch (InterruptedException e) {
              e.printStackTrace();
          }
      }
  }
  ```
  
**Demo:**

  ```java
  public class Main {
      public static void main(String[] args) {
          new Master().run();
      }
  }
  ```
  
**Output:**

  ```
  Thread-0 has died.
  Thread-1 has died.
  Thread-2 has died.
  Thread-3 has died.
  Thread-4 has died.
  The master will now die...
  ```
