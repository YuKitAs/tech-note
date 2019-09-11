# Server Password Encryption

In order not to specify server password in plaintext in `~/.m2/settings.xml`, we need to use a master password to encrypt the server password. The master password can be generated using the following command:

```console
$ mvn --encrypt-master-password
```

Then Maven will prompt for a master password and produce an encrypted master password like:

```console
$ {jSMOWnoPFgsHVpMvz5VrIt5kRbzGpI8u+9EF1iFQyJQ=}
```

We need to copy the encrypted master password into `~/.m2/settings-security.xml` like:

```xml
<settingsSecurity>
  <master>{jSMOWnoPFgsHVpMvz5VrIt5kRbzGpI8u+9EF1iFQyJQ=}</master>
</settingsSecurity>
```

Notice if there is `{` or `}` symbol in the encrypted password, they must be escaped with `\{` and `\}`.

Once we saved the `settings-security.xml`, we can encrypt the server password similarly:

```console
$ mvn --encrypt-password
```

Copy the encrypted password into `settings.xml`, other information can be added outside the curly brackets like:

```xml
<password>Expires on 2018-11-11 {COQLCE6DU6GtcS5P=}</password>
```
