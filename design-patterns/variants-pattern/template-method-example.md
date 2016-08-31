# Template Method example

***Participants:***

* AbstractClass: defines abstract primitive opertaions that concrete subclasses define to implement steps of an algorithm; implements a template method defining the skeleton of an algorithm.
* ConcreteClass: implements the primitive opertaions to carry out subclass-specific steps of the algorithm.

***AbstractClass:***

  ```java
  public abstract class Game {
    abstract void start();

    abstract void end();

    final void play() {
      start();
      end();
    }
  }
  ```
  
  
***ConcreteClass:***

  ```java
  public class PokemonGo extends Game {
    @Override
    void start() {
      System.out.println("Pokemon Go started.");
    }

    @Override
    void end() {
      System.out.println("Pokemon Go ended.");
    }
  }
  ```
  
***Demo:***

  ```java
  public class Main {
    public static void main(String[] args) {
      Game game = new PokemonGo();
      game.play();
    }
  }
  ```
  
***Output:***

  ```
  Pokemon Go started.
  Pokemon Go ended.
  ```