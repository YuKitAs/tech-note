# Refer to Names Containing `-`

In Helm template, it's not allowed to write something like `{{ .Values.foo-bar }}` with dash (`-`) in the name.

There are two tricks to avoid this syntax error. One way is to set an alias like `fooBar`. The other way is to write it as `{{ index .Values "foo-bar" }}` with quotes.
