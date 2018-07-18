# Use Bash in VS Code Terminal

Powershell is used as the default integrated terminal in Visual Studio Code on Windows. To use Bash, choose `File > Preferences > Settings`, add the following line into the right "User Settings"("Benutzereinstellungen") panel to overwrite the default path of Powershell:

```json
{
  "terminal.integrated.shell.windows": "C:\\path\\to\\bash.exe"
}
```

Save the settings, open the terminal, click the `+` button or use `Ctrl + Shift + Ö` to open a terminal, then choose `bash` from the dropdown menu. The next time when we open a new terminal it will use Bash by default, and when we reopen VS Code there'll be only Bash :)
