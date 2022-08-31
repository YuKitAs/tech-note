# Init Private Fields

```java
public class DummyService {
  private DummyObject dummyField;

  public DummyService() {
    // init dummyField
  }
}
```

We can mock private fields that are initialized in the constructor using `FieldSetter` (from `org.mockito.internal.util.reflection`, **deprecated in mockito-core 4.3.1**):


```java
@InjectMocks
private DummyService dummyService;

@Mock
private DummyObject dummyField;

@Before
public void setUp() throws NoSuchFieldException {
    FieldSetter.setField(dummyService, dummyService.getClass().getDeclaredField("dummyField"), dummyField);
}
```
