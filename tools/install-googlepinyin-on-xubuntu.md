# Install Google Pinyin on Xubuntu

1. Run the following command to install Google Pinyin:

  ```console
  $ sudo apt install fcitx-googlepinyin
  ```

2. In `Settings -> Language Support -> Keyboard input method system`, choose `fcitx`.

3. Log out and log in, a Linux penguin icon will appear on the top right of the Xfce panel.

4. Choose `ConfigureFcitx -> Input Method`, click `+` button to add new input method.

5. Unselect `Only Show Current Language` and search for `Google Pinyin`.

6. By default, `Ctrl+Space` or `L_Shift` is used to trigger input method, `Ctrl+Shift` to scroll between input methods.
