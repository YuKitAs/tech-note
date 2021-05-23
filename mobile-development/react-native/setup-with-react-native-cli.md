# Setup with React Native CLI

Compared to Expo CLI, React Native CLI requires Android Studio or Xcode.

There's no need to install the `react-native-cli` package globally. Instead, use `npx` to create a new project:

```console
$ npx react-native init <ProjectName> [--template react-native-template-typescript]
```

## Android

1. In Android Studio (4.1), make sure the following packages are installed (`File > Settings > Appearance & Behavior > System Settings > Android SDK`):

  `SDK Platforms`
  * Android 10.0 (Q)
    * Android SDK Platform 29
    * Intel x86 Atom_64 System Image or Google APIs Intel x86 Atom System Image

  `SDK Tools`
  * Android SDK Build-Tools 29.0.2

2. In `./bashrc`, add the following environment variables:

  ```
  export ANDROID_HOME=$HOME/Android/Sdk
  export PATH=$PATH:$ANDROID_HOME/emulator
  export PATH=$PATH:$ANDROID_HOME/tools
  export PATH=$PATH:$ANDROID_HOME/tools/bin
  export PATH=$PATH:$ANDROID_HOME/platform-tools
  ```

3. Start [Metro](https://facebook.github.io/metro/docs/concepts/) (a JavaScript bundler):

  ```console
  $ npx react-native start
  ```

  or

  ```console
  $ npm start
  ```

4. Build and start Android app:

  ```console
  $ npx react-native run-android
  ```

  or

  ```console
  $ npm run android
  ```

  If running on a physical device, do the following steps first:
  
  4.1 Connect the device, get device id and mode id (e.g. `1234:5678`) with `lsusb`
  
  4.2 Set device id and mode id in `/etc/udev/rules.d/51-android-usb.rules` with the following line: 
  
  ```
  SUBSYSTEM=="usb", ATTR{idVendor}=="1234", MODE="5678", GROUP="plugdev"
  ```
  
  4.3 Verify connection with `adb devices`
  
  4.4 Make sure it can connect to the development server:

  ```console
  $ adb reverse tcp:8081 tcp:8081
  ```
  
Debugger: http://localhost:8081/debugger-ui/
