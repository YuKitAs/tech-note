# Test Randomness

One option is to mock the random number generator (RNG) and pass the random object into the predictable deterministic RNG.

The following class will use the random object by accepting a `Random random` parameter:

  ```java
  import java.util.Random;

  public class RandomNumberPrinter {
    private Random random;

    public RandomNumberPrinter(Random random) {
      this.random = random;
    }

    public int generateRandomNumber() {
      return random.nextInt();
    }
  }
  ```
  
Mock a RNG with deterministic results, which extends Java's `Random` class and overrides its `nextInt()` method:

  ```java
  import java.util.Random;

  public class DeterministicRNG extends Random {
    private int num = 0;

    public DeterministicRNG() {
        super();
    }

    public int nextInt() {
        return num++;
    }
  }
  ```
  
Now we can test the `generateRandomNumber()` method in the `RandomNumberPrinter` class by passing a completely deterministic RNG to its constructor:

  ```java
  import org.junit.Before;
  import org.junit.Test;

  import static org.junit.Assert.assertEquals;

  public class RandomNumberPrinterTest {
    private RandomNumberPrinter printer;

    @Before
    public void setUp() {
      DeterministicRNG rng = new DeterministicRNG();
      printer = new RandomNumberPrinter(rng);
    }

    @Test
    public void generateRandomNumber() {
      assertEquals(0, printer.generateRandomNumber());
      assertEquals(1, printer.generateRandomNumber());
      assertEquals(2, printer.generateRandomNumber());
    }
  }
  ```
  
The expected random number will start from 0 for every test case.

