# Setup with Expo Client

1. Install Expo CLI:

  ```console
  $ npm install -g expo-cli
  ```

2. Create React Native project:

  ```console
  $ expo init my-project
  ```

3. Run app in the browser (`http://localhost:19002/`):

  ```console
  $ npm start
  ```

## Android

1. Enable USB debugging on the Android device and connect it to computer via USB. Get device ID and configure udev rules. See [official tutorial](https://reactnative.dev/docs/running-on-device).

4. Preview app on Android device:

  ```console
  $ expo start --localhost --android
  ```

  An Expo client app will be installed on the Android, scan the QR code using the Expo app.

## iOS

1. Install the Expo client app on the iOS device. Since there is no "scan the QR code" option in the app, create an Expo account first.

2. Start the app with `npm start` and use `Send link with email` to send an Expo link (authentication required). Open the link in the Expo app.
