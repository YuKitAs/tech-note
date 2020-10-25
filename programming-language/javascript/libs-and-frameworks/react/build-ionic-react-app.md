# Build Ionic React App

## Build a Web Project

1. Install Ionic CLI:

  ```console
  $ npm install -g @ionic/cli
  ```

2. Create a new project with React components:

  ```console
  $ ionic start <project-name> blank --type=react [--capacitor]
  ```

3. Run the web app on a local server (by default at `localhost:8100`):

  ```console
  $ ionic serve
  ```

## Build a Native App

1. Enable [Capacitor](https://capacitorjs.com/) (Ionic’s cross-platform app runtime) if not added when initializing the web project:

  ```console
  $ ionic integrations enable capacitor
  ```

2. Build project and add mobile platforms:

  ```console
  $ ionic build
  $ ionic cap add android
  $ ionic cap add ios
  ```

  Individual apps are created in `android` and `ios` directories.

3. Run the mobile apps:

* Run Android app with Android Studio (>= 3.6):

  1. Add the path to Android Studio (>= 3.6) in `capacitor.config.json` like:

  ```json
  "linuxAndroidStudioPath": "/path/to/android-studio/bin/studio.sh"
  ```

  2. Run:

  ```console
  $ ionic cap open android
  ```

* Run iOS app with Xcode:

  ```console
  $ ionic cap open ios
  ```
