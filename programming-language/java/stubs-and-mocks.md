# Stubs and Mocks

Stubs and mocks are both types of [test doubles](https://en.wikipedia.org/wiki/Test_double). According to Wikipedia, "Classification between mocks, fakes, and stubs is highly inconsistent across the literature." Personally I also felt that the difference between mocks and stubs is quite vague, especially when we don't use any mocking framework. So I just found some *common explanations* for them.

**Stub**

A Stub is a *replacement* for an existing dependency or collaborator. They are injected in the test to return controlled values to the testing object, for *state verification*.

A stub example from [Martin Fowler's article](https://martinfowler.com/articles/mocksArentStubs.html):

```java
public interface MailService {
  public void send (Message msg);
}

public class MailServiceStub implements MailService {
  private List<Message> messages = new ArrayList<Message>();
  public void send (Message msg) {
    messages.add(msg);
  }
  public int numberSent() {
    return messages.size();
  }
}
```

In the test:

```java
public void testOrderSendsMailIfUnfilled() {
    Order order = new Order(TALISKER, 51);
    MailServiceStub mailer = new MailServiceStub();
    order.setMailer(mailer);
    order.fill(warehouse);
    assertEquals(1, mailer.numberSent());
}
```

**Mock**

Mocks are part of the test, we have to set our expectations and then verify if the correct methods have been invoked in the mock. A widely used Java mocking framework is Mockito.
