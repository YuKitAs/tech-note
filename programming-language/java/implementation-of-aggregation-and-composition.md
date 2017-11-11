# Implementation of Aggregation and Composition

Aggregation and composition are two special [associations](https://en.wikipedia.org/wiki/Association_(object-oriented_programming). Composition is stronger than aggragation. These relationships can be illustrated by the following UML diagram (assuming every person can/should only have one name):

![](../master/assets/association.png)

The implementation in Java is normally with some kind of `Collection`, `ArrayList` for example.

Aggregation between `Company` and `Person` (1:N) and composition between `Person` and `Name` (1:1):

```java
public class Company {
    private List<Person> empolyees = new ArrayList<>();

    public Company() {
    }

    public List<Person> getEmpolyees() {
        return empolyees;
    }

    public void recruitEmpolyee(Person empolyee) {
        if (!this.empolyees.contains(empolyee)) {
            this.empolyees.add(empolyee);
            empolyee.setCompany(this);
        }
    }
}

public class Person {
    private Company company;
    private final String name;

    public Person(String name) {
        this.name = name;
    }

    public void setCompany(Company company) {
        this.company = company;
    }

    public Company getCompany() {
        return company;
    }

    public String getName() {
        return name;
    }
}
```

A person can exist without a company but a name just lives/dies with the person.
