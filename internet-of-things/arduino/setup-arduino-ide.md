# Setup Arduino IDE

1. Download the latest Arduino IDE from [official site](https://www.arduino.cc/en/Main/Software).

2. Take ARDUINO 1.8.9 on Ubuntu 18.04 for example. In the root of the extracted directory `arduino-1.8.9`, run `./install.sh`. The following warning can be ignored (might have been removed in a newer release):

  ```
  rm: cannot remove '/usr/local/bin/arduino': No such file or directory
  Removing symlink failed. Hope that's OK. If not then rerun as root with sudo.
  ```

  A desktop shortcut for Arduino IDE will be created. If the desktop icon doesn't display properly, try to change the owner of the shortcut file:

  ```console
  sudo chown $USER arduino-arduinoide.desktop
  ```
