# Rails 5 API Setup

Run the following commad to initialize an API-only application:

```console
$ rails new <project-name> --api
```

If we are going to use RSpec instead of the default test framework, add `-T`.

If we are going to use a NoSQL database, add `--skip-active-record`.

Generate model, controller, resources in routes and specs:

```console
$ rails g scaffold <model-name>
```
