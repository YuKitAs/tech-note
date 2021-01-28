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

3. Start Metro Bundler:

  ```console
  $ npx react-native start
  ```

  or

  ```console
  $ npm start
  ```

4. Build Android app:

  ```console
  $ npx react-native run-android
  ```

  or

  ```console
  $ npm run android
  ```

  If a physical device is connected, make sure it can connect to the development server:

  ```console
  $ adb reverse tcp:8081 tcp:8081
  ```
