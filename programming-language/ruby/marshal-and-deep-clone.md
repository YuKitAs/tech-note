# Marshal and Deep Clone

`Marshal` is a standard class used to serialize and deserialize Ruby objects. For example:

```ruby
marshalled = Marshal.dump([42, "abc", Object.new]) # => "\x04\b[\bi/I\"\babc\x06:\x06ETo:\vObject\x00"
Marshal.load(marshalled) # => [42, "abc", #<Object:0x000000019d21e0>]
```

Thus it can be used for deep clone of objects as follows, since the methods `dup` and `clone` provided by Ruby only do shallow clone.

```ruby
Marshal.load(Marshal.dump(@object))
```

However, marshalling is not for the objects that cannot be serialized (not marshallable), e.g. blocks and objects with single methods.
