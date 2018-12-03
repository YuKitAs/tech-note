# Use Custom Annotation to Validate Request Fields

1. Define an annotation for the field to be validated. Take a `username` field as example:

  ```java
  @Retention(RetentionPolicy.RUNTIME)
  @Target(ElementType.FIELD)
  @Constraint(validatedBy = UsernameValidator.class)
  public @interface Username {
      String message() default "Invalid username";

      Class<?>[] groups() default {};

      Class<? extends Payload>[] payload() default {};
  }
  ```

2. Define a `UsernameValidator` class which implements `ConstraintValidator` and override the `isValid()` method. In this example a valid `username` should only consist of numbers and/or letters and the length must be between 3 to 64, so we will simply define a custom pattern without using `ConstraintValidatorContext`:

  ```java
  public class UsernameValidator implements ConstraintValidator<Username, String> {
      private static final String USERNAME_PATTERN = "[a-zA-Z0-9]{3,64}";
      private static final Pattern PATTERN = Pattern.compile(USERNAME_PATTERN);

      @Override
      public boolean isValid(String s, ConstraintValidatorContext constraintValidatorContext) {
          return s != null && PATTERN.matcher(s).matches();
      }
  }

  ```

3. In the data model class, add the `@Username` annotation to the `username` field.

4. In the controller class, add `@Valid` before the `@RequestBody` parameter which needs to be validated.

If an invalid field in the request body fails validation, we will get status `400 Bad Request` with the default message `"Invalid username"` as well as the detailed error information.
