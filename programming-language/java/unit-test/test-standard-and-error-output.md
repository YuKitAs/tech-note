# Test Standard and Error Output (with JUnit)

One way is to use `ByteArrayOutputStream`:

  ```java
  private static final String OUT_MESSAGE = "Hello world!";
  private static final String ERROR_MESSAGE = "There is something wrong.";

  private final ByteArrayOutputStream stdout = new ByteArrayOutputStream();
  private final ByteArrayOutputStream stderr = new ByteArrayOutputStream();
  
  @Before
  public void setUp() {
    System.setOut(new PrintStream(stdout));
    System.setErr(new PrintStream(stderr));
  }
  
  @Test
  public void out() {
    System.out.println("hello world!");
    assertEquals(OUT_MESSAGE + "\r\n", stdout.toString());
  }

  @Test
  public void err() {
    System.err.println("Something is wrong.");
    assertEquals(ERROR_MESSAGE + "\r\n", stderr.toString());
  }
  
  @After
  public void tearDown() {
    System.setOut(null);
    System.setErr(null);
  }
  ```
