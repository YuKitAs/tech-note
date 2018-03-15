# Kernel Module

By using `Object.ancestors` we can see a Kernel module in the ancestors chain of Object, because the Kernel module is included in Object class, so its methods are available in every Ruby object, e.g. `:require` and `:puts`. These methods can be called without a receiver.
