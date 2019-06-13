# Regex Groups and Backreferences

`(regex)` or `\(regex\)` groups the regex and captures the matched text that can be reused with a numbered backreference.

For example, `(foo|bar)=\1` matches `foo=foo` or `bar=bar`, the `\1` hereby means backreferencing the first captured group `foo` or `bar`.

By using `(?:regex)`, the group matched will no longer be captured for referencing later on, which is called *Non-capturing group*.
