# Use of Camera Module

* Enable the Camera interface in `Preferences > Raspberry Pi Configuration` and reboot

* Use [`raspistill`](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md) to take photos:

  ```console
  $ raspistill -o Desktop/image.jpg
  ```

  The default resolution is 2592 x 1944.
  
  Use `-w` and `-h` to set image width and height.
  
  Use `-vf` to vertically flip the image (might be helpful if the camera has to be installed upside down in order to fit the stand).
  
  Use `-n` to disable preview window.

* Use [`raspivid`](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md) to record videos:

  ```console
  $ raspivid -o Desktop/video.h264 [-t <length>]
  ```

  The default length is 5000 (ms).

  To obtain a MP4 format video, install `MP4Box`:

  ```console
  $ sudo apt install -y gpac
  $ MP4Box -add video.h264 video.mp4 && rm video.h264
  ```
