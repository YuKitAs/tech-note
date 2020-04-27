# Boolean Json Property

For Boolean attributes in the DTO, should I choose `Boolean` or `boolean` as data type? Consider the following situations with the primitive `boolean`.

1. The `boolean` attribute cannot be null.

  Which means, if it's an optional field, it cannot use the annotation `@Nullable`, and no null value can be stored into the database; if it's a required field, the `@NotNull` constraint (from `javax.validation.constraints`) won't work either, because when the field is not provided in the request, its default value will always be `false`, no exception will ever be thrown.

  In a word, it's definitely better to use `Boolean` when the default value should be null in the database, or, the field is required in the request and an error is expected if it's not provided there.

2. When using `boolean`, Jackson will remove `is` in the name of the serialized Json property by default.

  For example, the `boolean isSuperAdmin` attribute will be mapped to `super_admin` or `superAdmin` in Json, unless using the annotation like `@JsonProperty("is_super_admin")` explicitly. The names will be more consistent if using `Boolean`.
