# Get `SHA-1` Certificate Fingerprint

The first time we run or debug our Android project in Android Studio, the debug keystore and certificate will be automatically generated in `$HOME/.android/debug.keystore`.

If we are not in the production mode, we need to add the `SHA-1` fingerprint stored in `debug.keystore` to Firebase. It can be output using the following command:

```console
$ keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android
```
