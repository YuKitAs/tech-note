# Setup Arduino IDE

1. Download the latest Arduino IDE from the [official site](https://www.arduino.cc/en/Main/Software).

2. Take ARDUINO 1.8.9 on Ubuntu 18.04 for example. In the root of the extracted directory `arduino-1.8.9`, run `./install.sh`. The following warning can be ignored (might have been removed in a newer release):

  ```
  rm: cannot remove '/usr/local/bin/arduino': No such file or directory
  Removing symlink failed. Hope that's OK. If not then rerun as root with sudo.
  ```

  A desktop shortcut for Arduino IDE will be created. If the desktop icon doesn't display properly, try to change the owner of the shortcut file:

  ```console
  sudo chown $USER arduino-arduinoide.desktop
  ```

3. Connect Arduino, open Arduino IDE, make sure the board and the serial port are selected correctly in `Tools > Board` and `Tools > Port`.

4. Select an example from `File > Examples` for test. On uploading code, it may show an error about serial port permission, because `/dev/ttyACM*` (e.g. `/dev/ttyACM0`) can only be read and written by a special group called `dialout`. The official suggestion is to add our user to this group:

  ```console
  sudo usermod -a -G dialout $USER
  ```

  A quick and dirty way is, of course, to change the permission of the file (`666` or `a+rw`).

5. Place new library files in `arduino-1.8.9/libraries`, for example:

  ```
  arduino-1.8.9/libraries/Cool_Library/
  ├── keywords.txt
  ├── CoolLibrary.cpp
  ├── CoolLibrary.h
  └── README.md
  ```

  Then the header file can directly be included like

  ```
  #include <CoolLibrary.h>
  ```
